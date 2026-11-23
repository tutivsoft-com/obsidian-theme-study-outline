# Original Study Outline design plan

An Obsidian theme with a clear heading hierarchy and easy-to-scan study notes.

This plan records the initial design from 13 November 2026. Study Outline was first released on 14 November 2026 and published in the Obsidian Community directory on 20 November 2026. See the [README](README.md) for current installation and source checks.

Search keywords: Obsidian theme, study notes, headings, outline, students, structured notes.

## Who this is for

Students and researchers working with long notes, outlines and nested concepts.

## User need and evidence

Users directly complain that different heading levels look almost identical and make the structure of a note hard to recognise.

- [Request to distinguish heading levels](https://www.reddit.com/r/ObsidianMD/comments/1uumbno/is_there_a_way_to_better_differentiate_headings/)

The Reddit request was part of the original research and illustrates one user's experience.

## Planned appearance and features

- Give H1 through H6 clearly different sizes, weights and spacing.
- Offer restrained optional heading colours while retaining a hierarchy that works without colour.
- Make list nesting, indentation guides and bullets easy to follow.
- Use distinct but readable callouts for definitions, examples, questions and warnings where supported.
- Keep tables, maths and code readable alongside prose.
- Keep heading appearance consistent between editing, Live Preview and Reading view where each view permits.

## Mode scope

Plan both light and dark modes.

## Original implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

## Official references

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Original acceptance checklist

- Review a sample note containing every heading level and several nested list levels.
- Check hierarchy in grayscale and at enlarged font sizes.
- Verify headings and callouts across editor and Reading view.
- Confirm every claimed feature has been implemented and tested.
- Review screenshots for private information and verify all published documentation and asset paths.
- Verify the default branch, release revision and uploaded assets before calling any future release complete.
