---
title: Transitions
parent: Operations
nav_order: 7
---

# Transitions
{: .no_toc }

Soften the cuts between segments and fade the video in and out.

1. TOC
{:toc}

---

{% include screen.html name="transition-buttons" alt="Round transition buttons on the timeline: on each split, at the start and at the end. One is filled orange because it has a transition." %}

## Where transitions go

With deleted segments hidden, the timeline shows a **round button**:

- at the **start** of the video (marker 2): fade in,
- on **every split** (marker 1): transition between two segments,
- at the **end**: fade out.

A button turns **orange** when it has a transition.

## Add a transition

1. Tap the round button.
2. Between segments, choose the **type**:
   - **Fade out-in**: the picture dips to black and comes back.
   - **Interleave** <span class="label label-yellow">PRO</span>: a crossfade, the end of one
     segment blends into the start of the next. The video gets shorter by the transition's duration.
3. Set the **Duration** (0.5–10 s; total, in the finished video).
4. Tap **Save**.

At the start and end there's no type to choose: the video fades in from black or out to black,
picture and sound together.

{% include screen.html name="transition" alt="The Add transition dialog with Fade out-in selected and a 1.0 s duration." %}

## Change or remove

Tap the orange button again, change the settings, or tap **Remove transition**.

{: .note }
> A transition can't be longer than the segments next to it allow. If they're short, the dialog
> says the transition is *currently limited*; it uses the longest duration that fits.

## Free and Pro

| Transition | Free | Pro |
|---|---|---|
| Fade in at the start, fade out at the end | ✓ | ✓ |
| **Fade out-in** between segments | ✓ | ✓ |
| **Interleave** (crossfade) between segments | | ✓ |

In Free, **Interleave** is shown with a **PRO** badge; tapping it explains the feature. See [Free and Pro]({{ "/editions/" | relative_url }}).
