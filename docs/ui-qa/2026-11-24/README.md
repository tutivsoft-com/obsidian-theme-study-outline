# Study Outline UI test

Tested on 24 November 2026 in Obsidian 1.15.1 on Windows 11 Pro, build 26300. The isolated Study Outline QA vault used synthetic notes, properties, a Canvas board and a Base. The installed theme was Study Outline 3.6.2.

Study Outline 3.6.1 drew its inset focus outline over the left edge of text in Source mode and Live Preview. Version 3.6.2 moves the outline outside the text and keeps the 2 px indicator. It also improves code operator contrast from 3.73:1 to 6.31:1 in light mode and from 3.92:1 to 6.14:1 in dark mode. The rerun checked both changes in the app. Six source checks passed with `python test_theme.py -v`.

## Results

| ID | Workflow | Verified result |
| --- | --- | --- |
| C01 | Appearance theme selector | Switched from Study Outline to Default and back. The installed theme and its CSS were active on return. |
| C02 | Base color scheme | Selected Dark, Light and Adapt to system. Light and Dark applied the expected theme palettes. |
| C03 | Heading hierarchy and larger note text | Moved the font size from 16 to 21 px and restored 16 px. Reading view retained descending H1 to H6 sizes. A grayscale review of the capture also preserved the hierarchy. |
| C04 | Light Live Preview | Checked six headings, nested list indentation and the editor focus indicator. |
| C05 | Dark Reading view | Checked six heading levels, the H2 divider, and nested list markers. |
| C06 | Dark Source mode | Checked Markdown markers, edit and undo, selection, and the corrected focus outline. |
| C07 | Indentation guides | Turned guides off and on in Editor settings. Reading view followed both changes. |
| C08 | Nested list folding | Collapsed and expanded a nested list in Reading view. |
| C09 | Nested task controls | Checked and restored a task and verified the checked and unchecked states. |
| C10 | Properties and callouts | Read three properties and four callout types in light Reading view. Expanded and collapsed the question callout. |
| C11 | Rich Markdown | Checked a table, inline math, syntax-highlighted code, marked text and both link styles in dark Reading view. Measured code operator contrast in both palettes. |
| C12 | Note navigation | Opened an internal link and used Back to return to the original note. |
| C13 | Search | Checked the focused search field, two matching notes and the no-results state. |
| C14 | Quick switcher and tabs | Selected a note by keyboard, opened another in a new tab, switched tabs and closed the added tab. |
| C15 | Command palette and sidebar | Ran the sidebar command and reopened the file sidebar with its control. |
| C16 | Canvas | Opened a sample board with three cards and two connectors and checked its zoom control. |
| C17 | Bases | Opened a table with three sample notes and their properties. |
| C18 | Mobile editor layout | Opened a note from the file drawer in Obsidian's mobile emulation at a 430 px portrait viewport. Measured 8 px of inline padding on each side. |
| C19 | Mode and palette crossover | Verified the corrected outline in light Source mode and dark Live Preview. |

All 19 workflows passed. The desktop tests cover Reading view, Live Preview and Source mode in both palettes. Native Android, iOS, macOS and Linux remain unverified.

## Screenshots

The ten screenshots come from the running Obsidian app and contain synthetic vault data. The files use lossless WebP and omit image metadata.

| Image | Tested state |
| --- | --- |
| [01](01-dark-reading-hierarchy.webp) | Dark Reading view with six heading levels and nested bullet guides |
| [02](02-dark-source-selection.webp) | Dark Source mode with selected text and the corrected editor outline |
| [03](03-light-live-preview.webp) | Light Live Preview with heading and list styles |
| [04](04-light-appearance.webp) | Appearance with Study Outline selected in the Light scheme |
| [05](05-dark-checklist.webp) | Dark nested checklist after selecting a task |
| [06](06-light-properties-and-callouts.webp) | Light properties and expanded question callout |
| [07](07-dark-table-math-code.webp) | Dark Reading view with a table, math, links and code |
| [08](08-light-search.webp) | Light Search with the query `ecology` |
| [09](09-dark-canvas.webp) | Dark Canvas with three study cards and connectors |
| [10](10-light-mobile-emulation.webp) | Light editor in Obsidian's mobile emulation |
