---
title: The editor
parent: Operations
nav_order: 2
---

# The editor: playback and the timeline
{: .no_toc }

1. TOC
{:toc}

---

{% include screen.html name="editor" alt="The editor with the timeline in the lower half." %}

## Play and pause

Tap **▶** under the preview. Playback already follows your edits: deleted segments are skipped,
sped-up segments play fast, subtitles appear, and fades dim the picture.

The time shown is the position in the **finished video** and its total length
(for example `0:21.4 / 0:48.0`). It changes as you delete and speed up segments.

## Move around the video

- **Tap** anywhere on the timeline to jump there.
- **Drag** along the timeline to scrub.

The white line with a dot is the **playhead**: the current position. The segment under it is
**selected** (orange outline); the tools act on the selected segment.

## Read the timeline

| You see | It means |
|---|---|
| Picture strip | Frames from the video, so you can find places by sight |
| `1×`, `4×`, `0.5×` in the corner | The segment's speed (orange when it isn't 1×) |
| Orange line with a ▼ at the top | A split between two segments |
| Short red line | Deleted footage is hidden here |
| Round button on a split | Transition (see [Transitions]({{ "/operations/transitions/" | relative_url }})) |
| ⓘ on the selected segment | [Segment details]({{ "/operations/segment-info/" | relative_url }}) |
| Times above the strip | Times in the *original* video |

## Zoom in

On a long video a split needs precision. Use any of:

- **🔍+ / 🔍−** under the timeline (each tap doubles or halves the zoom),
- **pinch** the timeline with two fingers,
- the **slider** between them to move along the zoomed timeline.

## Undo

**↶** (top right of the controls) takes back the last change: a split, a delete, a speed change,
a subtitle, a transition. Tap it repeatedly to go further back.
