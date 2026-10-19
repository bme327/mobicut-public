---
title: The editor
parent: Operations
nav_order: 3
---

# The editor: playback and the timeline
{: .no_toc }

1. TOC
{:toc}

---

{% include screen.html name="editor" alt="The editor with the timeline in the lower half." %}

## Play and pause

Tap **▶** under the preview. Playback already follows your edits: deleted segments are skipped,
sped-up segments play fast, subtitles appear on the video with their animation, fades dim the
picture and interleaves crossfade.

The two small times next to the buttons are the position in the **finished video** (top) and
its total length (bottom), for example `0:21.4` over `0:48.0`. They change as you delete and speed
up segments.

## Jump

The buttons around **▶** jump the playhead, also while playing:

| Button | Jumps |
|---|---|
| **⏮** | To the beginning of the finished video (its first kept frame) |
| **↺ 5** | 5 seconds back |
| **↻ 5** | 5 seconds forward |
| **⏭** | To the end (playback stops there) |

The 5 seconds are 5 seconds of the **finished** video: deleted parts are skipped, and over a
4× segment a jump moves 20 seconds through the original.

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
| `1× · muted` | The segment's sound is [muted]({{ "/operations/mute/" | relative_url }}) |
| `Picture`, `Zoom in`, `Zoom out`, `Slide in` | A [picture]({{ "/operations/pictures/" | relative_url }}) segment and its effect |
| White line across the strip | Where one video or picture ends and the next begins ([several videos]({{ "/operations/videos/" | relative_url }})) |
| Orange line with a ▼ at the top | A split between two segments |
| Short red line | Deleted footage is hidden here |
| Round button on a split | Transition (see [Transitions]({{ "/operations/transitions/" | relative_url }})) |
| ⓘ on the selected segment | [Segment details]({{ "/operations/segment-info/" | relative_url }}) |
| Times above the strip | Times in the *original* video (videos and pictures laid end to end) |
| Green chips under the subtitles | [Soundtracks]({{ "/operations/soundtracks/" | relative_url }}); the lane only shows once you add one |

## Zoom in

On a long video a split needs precision. Use any of:

- **🔍+ / 🔍−** under the timeline (each tap doubles or halves the zoom),
- **pinch** the timeline with two fingers,
- the **slider** between them to move along the zoomed timeline.

## Undo

**↶** (top right of the controls) takes back the last change: a split, a delete, a speed change,
a subtitle, a transition, a mute, a picture, a soundtrack or an added video. Tap it repeatedly to go further back.
