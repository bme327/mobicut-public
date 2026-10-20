---
title: Subtitles
parent: Operations
nav_order: 8
---

# Subtitles
{: .no_toc }

Short texts over the video: a place, a name, the altitude. You place and style them right on the
video, and what you see in the preview is exactly what the export burns in. They can also be
exported as a separate `.srt` file.

1. TOC
{:toc}

---

{% include screen.html name="subtitles-timeline" alt="Subtitle chips on the subtitle track under the timeline, and the subtitle shown on the video in the preview." %}

## Add a subtitle

1. Move the playhead to where the text should appear.
2. Tap **Subtitle** in the toolbar (marker 2).
3. The subtitle editor opens under the preview, with the keyboard ready: type the text.
4. Tap **Done**.

A new subtitle starts at the playhead, stays on screen for **5 s**, and looks like the last subtitle
you edited (same position, look and motion). A blue chip appears on the subtitle track (marker 1). It starts with a small **T**, so you can
tell it's a subtitle even when the chip is too short to show the text.

If you tap **Done** without typing anything, the empty subtitle is dropped.

## The subtitle editor

Tap a subtitle **on the video** (while paused) or its **blue chip** on the timeline to open it.
The editor replaces the timeline; the preview stays above it and shows every change at once.

{% include screen.html name="subtitle-editor" alt="The subtitle editor: the subtitle on the video with a dashed box and orange corner handles, and below it the Text tab with the text, Duration and Starts at." %}

1. **Drag the subtitle** to move it on the video. It snaps to the horizontal centre.
2. **Drag a corner** to resize its box. The text wraps to the box's width; if it needs more room,
   the box grows taller.
3. **Tabs**: *Text*, *Look* and *Motion*.
4. **Starts at**: move the subtitle in time (see [below](#move-it-in-time)).
5. **▶** plays the subtitle with its entrance and exit, from half a second before to half a
   second after it. The editor stays open.
6. **Done** closes the editor. Everything you changed is **one** step for **Undo**.

The bin icon deletes the subtitle. The phone's **Back** button closes the editor, like **Done**.

### Text

- The text itself; it wraps to the box.
- **Duration**: how long it stays on screen in the finished video, **−** / **+** in half-second
  steps (0.5–60 s).
- **Starts at**: when it appears.

{: .note }
> Times count the **finished** video. A 5 s subtitle over a 4× segment still stays on screen for
> 5 s; it just covers more of the original footage.

### Look

{% include screen.html name="subtitle-look" alt="The Look tab: font chips, Bold and Italic, alignment, Size, text colour swatches and opacity sliders. The subtitle on the video is bold serif yellow without a background." %}

- **Font**: Sans, Serif, Mono, Condensed, Casual, Cursive, Small caps.
- **Bold**, **Italic** and **alignment** (left, centre, right) inside the box.
- **Size**: 2–16 % of the video's shorter side, so it looks the same at 720p and 4K.
- **Text colour** and **Text opacity**.
- **Background colour** and **Background opacity**: the rounded band behind the text. Below 40 %
  the text gets a soft shadow, so it stays readable over snow and sky.
- **Position**: *Top*, *Middle*, *Bottom* and *Centre* put the box there in one tap; drag it on the
  video for anything else.
- **Use this position, look and motion for all subtitles** copies this subtitle's style to every
  subtitle in the project.

### Motion

{% include screen.html name="subtitle-motion" alt="The Motion tab: Ease in Zoom with 0.4 s, Ease out Fade with 0.3 s, and the Wobble effect." %}

- **Ease in** and **Ease out**: how the subtitle appears and goes away.
  - *None*: just on and off,
  - *Fade*,
  - *Slide*: in from below, out downwards, fading,
  - *Zoom*: grows in, shrinks out,
  - *Type*: typed out letter by letter (on the way out it fades).

  Each has a **Duration** of 0.1–2 s; neither takes more than half the subtitle's time on screen.
- **Effect while shown**: *Wobble* (gently rocks), *Pulse* (breathes bigger and smaller),
  *Shake* (jitters), *Float* (bobs up and down).

While paused, the preview shows the subtitle still, so it's easy to place. Tap **▶** to see it move.

## Move it in time

Two ways:

- **Drag its chip** along the subtitle track under the timeline. The playhead follows, so the
  preview shows where it lands. Each drag is one step for **Undo**; a tap still opens the editor.
- In the editor, **Starts at** with **−1 s**, **−0.1**, **+0.1** and **+1 s**. The time shown is the
  time in the finished video, like the times under the preview.

Either way it keeps how long it's on screen, also when it moves onto a sped-up segment. Near the end
of the video it's cut short so it doesn't run past it.

## Several at once

Subtitles can overlap in time, for example a title at the top and a caption at the bottom. They all
show, each in its own box.

## Subtitles in the export

When you [export]({{ "/operations/export/" | relative_url }}), choose:

- **Burn into video**: the subtitles become part of the picture, with their position, look and
  motion, exactly as in the preview. Fades from [transitions]({{ "/operations/transitions/" | relative_url }})
  fade them too.
- **Separate .srt file**: saved to `Download/MobiCut` next to a clean video. An `.srt` file only
  holds the text and times; players show it in their own style.
- **Off**.

Subtitles from projects made before styling existed keep their classic look: white text on a dark
band near the bottom.
