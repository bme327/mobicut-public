---
title: Pictures
parent: Operations
nav_order: 9
---

# Add a picture
{: .no_toc }

Put a photo into the video: the summit shot, a map of the flight, a title card. A picture
becomes a segment of its own, shown for as long as you choose, standing still or moving.

1. TOC
{:toc}

---

## Insert a picture

1. Move the playhead to where the picture should go.
2. Tap **Add**, then **Picture at the pointer**.
3. Tap **Gallery** or **Browse files** and pick the picture. Its name shows under the buttons.
4. Set the **Duration** with **−** and **+** (0.5 s steps, from 0.5 s to 60 s; it starts at 3 s).
5. Choose an **Effect** (see below), then tap **Insert**.

{% include screen.html name="picture-add" alt="The Add picture dialog: Gallery and Browse files buttons, the picked picture's name, Duration 3.0 s, and the effects Still, Slow zoom in (selected), Slow zoom out and Slide in." %}

The video is split at the playhead and the picture goes in between; everything after it moves
on by the picture's duration, subtitles included. If the playhead is within a tenth of a second of
a split, the picture goes right at that split instead of making a tiny segment.

## Effects

| Effect | What it does |
|---|---|
| **Still** | No movement |
| **Slow zoom in** | Moves closer over the whole duration |
| **Slow zoom out** | Starts close and moves back |
| **Slide in** | Comes in from the right (in about a second), then stays |

The preview shows the effect as it will be in the export. Pictures are fitted inside the video's
frame, with black bars if their shape differs.

## On the timeline

A picture segment shows the picture and its effect as its label (**Picture**, **Zoom in**,
**Zoom out**, **Slide in**). A white line marks where it starts and ends
(see [Several videos]({{ "/operations/videos/" | relative_url }}#on-the-timeline)).

It works like any other segment:

- [delete and restore]({{ "/operations/delete/" | relative_url }}) it,
- put a [transition]({{ "/operations/transitions/" | relative_url }}) before or after it, for
  example a fade out-in, or an Interleave so it crossfades with the video,
- [subtitles]({{ "/operations/subtitles/" | relative_url }}) can run over it.

**Speed** and **Mute** don't apply to pictures and are greyed out when one is selected.

## Change or remove a picture

Select it and tap **ⓘ**. The [segment details]({{ "/operations/segment-info/" | relative_url }})
have **Duration & effect…** to change them, and **Remove this picture**.

{: .note }
> The duration can only change while the picture is one segment. If you split it, its
> duration is fixed (the dialog says so); its effect can still change.

Pictures are in both editions.
