# Mobile web reference recreation

Open `index.html` directly in a browser. No server, installation, build, or network connection is required. Use a 393 × 852 CSS-pixel viewport for the intended composition. There is no phone bezel.

All HTML, CSS, inline SVG icons, and JavaScript are in `index.html`. The seven PNG files in `assets/` contain only cropped product imagery and decorative artwork from `source-screen.png`. Text, prices, card surfaces, category tabs, buttons, search field, status bar, banner, and navigation are editable DOM elements. The full reference image is not loaded by the prototype.

Demo behaviors:
- Notify Me changes to “Notification enabled”.
- The delivery banner close button hides the banner.
- Categories scroll horizontally and support click selection and arrow-key navigation.
- Reloading resets all demo state; no browser storage is used.

Validation: Headless Google Chrome at 393 × 852, opened directly through a file URL. Verified actual pointer clicks on notification, banner close, and category selection; horizontal wheel scrolling; keyboard category selection; reload reset; all seven images loading; and absence of document horizontal overflow. Results and screenshot are in `.qa/results.json` and `.qa/initial-393x852.png`. The dependency-free Node CDP check is `.qa/check.mjs`; it expects a dedicated Chrome debug session on port 9223.

Limitations: Search accepts text but has no results service. Other navigation, account, address, microphone, and promotional controls are visual placeholders. Notification enables only demo state. Icons, brand lettering, and decorative title typography are approximations; font rendering depends on availability of Avenir Next, Avenir, or Arial. Product packaging text is embedded in the permitted photo crops. Physical mobile devices and Safari were not tested. Layout is optimized for the requested viewport.
