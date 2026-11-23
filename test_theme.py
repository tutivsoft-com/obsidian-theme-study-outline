import json
import re
import unittest
from pathlib import Path

from cssselect2 import compile_selector_list
from tinycss2 import parse_declaration_list, parse_stylesheet, serialize


ROOT = Path(__file__).resolve().parent
VERSION = r"[0-9]+\.[0-9]+\.[0-9]+"


def luminance(color):
    channels = [int(color[start:start + 2], 16) / 255 for start in (1, 3, 5)]
    linear = [
        value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return sum(value * weight for value, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(foreground, background):
    dark, light = sorted((luminance(foreground), luminance(background)))
    return (light + 0.05) / (dark + 0.05)


class ThemeTests(unittest.TestCase):
    def setUp(self):
        self.css = (ROOT / "theme.css").read_text(encoding="utf-8")
        self.rules = {}
        for rule in parse_stylesheet(self.css, skip_comments=True, skip_whitespace=True):
            self.assertEqual(rule.type, "qualified-rule", rule)
            selector = serialize(rule.prelude).strip()
            compile_selector_list(rule.prelude)
            declarations = self.rules.setdefault(selector, {})
            for item in parse_declaration_list(rule.content, skip_comments=True, skip_whitespace=True):
                self.assertEqual(item.type, "declaration", item)
                declarations[item.name] = serialize(item.value).strip()

    def test_manifest_and_source_version(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        for field in ("name", "version", "minAppVersion", "author"):
            self.assertTrue(manifest[field])
        self.assertRegex(manifest["version"], rf"^{VERSION}$")
        self.assertRegex(manifest["minAppVersion"], rf"^{VERSION}$")
        self.assertTrue(self.css.startswith(f"/* {manifest['name']} {manifest['version']}."))
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"Source version {manifest['version']}", readme)

    def test_heading_sizes_descend_without_relying_on_color(self):
        settings = self.rules["body"]
        sizes = []
        for level in range(1, 7):
            size = settings[f"--h{level}-size"]
            self.assertRegex(size, r"^[0-9]+(?:\.[0-9]+)?em$")
            sizes.append(float(size.removesuffix("em")))
        for larger, smaller in zip(sizes, sizes[1:]):
            self.assertGreater(larger, smaller)

    def test_text_and_component_borders_have_contrast_in_both_modes(self):
        for mode in ("light", "dark"):
            palette = self.rules[f"body.theme-{mode}"]
            for surface in ("--background-primary", "--background-secondary"):
                for foreground, minimum in (
                    ("--text-normal", 4.5),
                    ("--text-muted", 4.5),
                    ("--link-color", 4.5),
                    ("--background-modifier-border", 3),
                    ("--background-modifier-border-hover", 3),
                    ("--background-modifier-border-focus", 3),
                ):
                    with self.subTest(mode=mode, surface=surface, foreground=foreground):
                        self.assertGreaterEqual(contrast(palette[foreground], palette[surface]), minimum)

    def test_list_markers_keep_native_hover_and_collapse_styles(self):
        settings = self.rules["body"]
        self.assertEqual(settings.get("--list-marker-color"), "var(--text-muted)")
        self.assertGreater(float(settings["--list-spacing"].removesuffix("em")), 0)
        for selector, declarations in self.rules.items():
            if ".list-bullet" in selector:
                self.assertNotIn("background-color", declarations)

    def test_readme_assets_exist_at_the_documented_paths(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        local_links = [
            target for target in re.findall(r"\]\(([^)]+)\)", readme)
            if "://" not in target
        ]
        self.assertIn("screenshot.png", local_links)
        self.assertIn("screenshot-light.png", local_links)
        for target in local_links:
            with self.subTest(target=target):
                self.assertTrue((ROOT / target).is_file())
                if target.endswith(".png"):
                    with (ROOT / target).open("rb") as image:
                        self.assertEqual(image.read(8), b"\x89PNG\r\n\x1a\n")


if __name__ == "__main__":
    unittest.main()
