---
title: Subtitles
parent: Operations
nav_order: 7
---

# Subtitles
{: .no_toc }

Short texts over the video: a place, a name, the altitude. They can be burned into the picture or
exported as a separate `.srt` file.

1. TOC
{:toc}

---

{% include screen.html name="subtitles-timeline" alt="Subtitle chips on the subtitle track under the timeline, and the subtitle shown over the preview." %}

## Add a subtitle

1. Move the playhead to where the text should appear.
2. Tap **Subtitle** in the toolbar (marker 2).
3. Type the text (up to three lines).
4. Set **Duration**, how long it stays on screen in the finished video: **−** / **+** in
   half-second steps, 5 s by default.
5. Tap **Save**.

A blue chip appears on the subtitle track (marker 1), and the text shows over the preview while
it plays.

{% include screen.html name="subtitle-add" alt="The Add subtitle dialog with text, duration and start time." %}

{: .note }
> The duration counts time in the **finished** video. A 5 s subtitle over a 4× segment still
> stays on screen for 5 s; it just covers more of the original footage.

## Edit or delete a subtitle

Tap the **blue chip**. In the dialog you can:

- change the text or the duration,
- **Start at playhead** to move it to the current position,
- **Delete subtitle**.

{% include screen.html name="subtitle-edit" alt="The Edit subtitle dialog with Start at playhead and Delete subtitle." %}

## Subtitles in the export

When you [export]({{ "/operations/export/" | relative_url }}), choose:

- **Burn into video**: the text becomes part of the picture (works everywhere),
- **Separate .srt file**: saved to `Download/MobiCut` next to a clean video,
- **Off**.
