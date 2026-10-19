---
title: Export
parent: Operations
nav_order: 9
---

# Export the finished video
{: .no_toc }

Export builds a new video from your edits. The original is not touched.

{: .important }
> **Exports are very fast.** The video is rendered on the phone with its built-in video hardware.
> Nothing is uploaded, and deleted parts are skipped.

1. TOC
{:toc}

---

## Export

1. Tap **Export** at the top of the editor.
2. Check the length and number of segments at the top of the sheet, then choose:
   - **Resolution**: *Original*, or a smaller one (1080p, 720p) for a smaller file. Only
     sizes smaller than the original are offered.
   - **Frame rate**: *Original*, or *30 fps* (offered for 50/60 fps videos). 30 fps makes the
     file smaller and is plenty for sharing.
   - **Subtitles** (if the project has any): *Burn into video*, *Separate .srt file* or *Off*.
3. Tap **Export to gallery**.

{% include screen.html name="export" alt="The Export sheet with resolution, frame rate and subtitle options." %}

## While it exports

A progress bar shows how far it is. **Keep mobiCut open** until it finishes; the screen stays
on by itself. **Cancel** stops it.

{% include screen.html name="export-progress" alt="Exporting… dialog at 42 % with a Cancel button." %}

{: .note }
> If the phone can't encode the original settings (very high resolution or frame rate), the
> export steps down automatically and tells you what it changed.

## When it's done

The video is saved to **`Movies/MobiCut`** and appears in the gallery. From the dialog you can:

- **Play** it,
- **Share** it straight to a messaging app,
- **Close**.

{% include screen.html name="export-done" alt="Saved to gallery dialog with Play, Share and Close." %}

## The mobiCut logo

The Free edition adds a small **(mc) mobiCut** logo in the top right corner of the exported
video (you see it in the preview too, so there are no surprises). Pro exports without it. In
Free, the export sheet shows **Remove watermark** with a **PRO** badge.

No ads appear before, during or after the export, in either edition.
