# OpenDesign vs Codex Sol vs Codex Astra

Source files for the YouTube video [**Astra vs a Free AI Design Tool: Which Rebuilds This UI Better?**](https://youtu.be/rfoPJFIZMKU). The video compares three attempts to recreate the same mobile screen from a screenshot and prompt, with High reasoning selected for each run.

| Run | Folder | Setup |
| --- | --- | --- |
| OpenDesign | [`opendesign-codex/`](opendesign-codex/) | OpenDesign using Codex Sol High |
| Codex Sol | [`codex-only/`](codex-only/) | Sol High directly in Codex |
| Codex Astra | [`codex-astra/`](codex-astra/) | Astra High directly in Codex |

## View the pages

Clone or download this repository, then open the `index.html` file in any of the three folders in a browser. Each page is a standalone HTML/CSS/JavaScript prototype with local PNG assets. No installation, build step, server, or API key is needed. For a like-for-like view, set the browser viewport to **393 × 852 CSS pixels** using mobile device emulation.

The reference screenshot is included as `source-screen.png` in each folder. The three copies are identical; each run also has its own cropped assets in `assets/`. The pages use those crops rather than displaying the full reference screenshot as their UI.

## What is in this snapshot

These files preserve the local artifacts used around the video comparison. The `codex-only/` page includes the later delivery-banner revision to **₹299** and “Applied automatically at checkout.” The `opendesign-codex/` and `codex-astra/` pages in this repository still show the initial **₹199** banner. Keep that difference in mind when comparing these files with the initial and revised results shown in the video.

The prototypes are visual recreations, not a working grocery service. Some controls demonstrate local UI behavior, such as selecting categories, enabling the notification button, or dismissing the delivery banner. Search, checkout, account, and other service actions are not connected to a backend.

The Astra folder also includes its original [implementation and validation notes](codex-astra/README.md) and `.qa/` evidence.
