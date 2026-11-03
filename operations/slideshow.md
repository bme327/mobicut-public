---
title: Slideshow
parent: Operations
nav_order: 13.5
---

# Slideshow from pictures
{: .no_toc }

Turn a set of photos into a video in one go: the best shots of the day, a trip in pictures. Pick
the photos, say how long the video should be, and mobiCut makes a new project where every photo is
an ordinary [picture]({{ "/operations/pictures/" | relative_url }}) segment.

1. TOC
{:toc}

---

## Make a slideshow

1. On the start screen tap **New project**, then **Slideshow from pictures**.
2. Pick the pictures in the gallery, **up to 50**, in the order they should play.
3. Set the options (below) and tap **Create**.

{% include screen.html name="new-project" alt="The 'New project from…' sheet with Gallery, Browse files and Slideshow from pictures." %}

The editor opens with one segment per picture, in the order you picked them. The project is
called *Slideshow*; [rename it]({{ "/operations/projects/" | relative_url }}) as you like.

{% include screen.html name="slideshow" alt="The Slideshow dialog: 12 pictures with their thumbnails, Length of the video 1:00 with a slider and 'About 5.0 s per picture', Shape chips Landscape, Portrait and Square, Resolution chips 720p, 1080p and 4K with 1920×1080 · 30 fps under them, Effect chips Still, Zoom in, Zoom out and Slide in, and the Transitions between pictures switch." %}

## Options

- **Length of the video**: drag the slider. It starts at 5 seconds per picture and goes from 1 to
  20 seconds per picture; the line under it shows the time each picture gets. Every picture is shown
  for the same time.
- **Shape**: **Landscape** (16:9), **Portrait** (9:16) or **Square**. It starts on the shape of the
  first picture. Pictures of another shape are fitted inside the frame.
- **Resolution**: **720p**, **1080p** or **4K**, with the frame size in pixels under the chips. The
  video is 30 fps. **4K is Pro**; Free exports up to 1080p.
- **Effect**: the same movement for every picture: **Still**, **Zoom in**, **Zoom out** or
  **Slide in** (see [Pictures]({{ "/operations/pictures/" | relative_url }})).
- **Transitions between pictures**: puts a transition at every join and fades in at the start and
  out at the end, with the type and length last used in
  [Transitions at every join]({{ "/operations/transitions/" | relative_url }}).

The dialog remembers the resolution, effect and transitions for next time.

## After that

A slideshow is a normal project. You can change any picture's duration or effect in its
[Segment info]({{ "/operations/segment-info/" | relative_url }}), delete or add pictures, add
[texts]({{ "/operations/subtitles/" | relative_url }}),
[graphics]({{ "/operations/graphics/" | relative_url }}),
[text slides]({{ "/operations/text-slides/" | relative_url }}),
[music]({{ "/operations/soundtracks/" | relative_url }}) and even
[videos]({{ "/operations/videos/" | relative_url }}). The frame keeps the shape and resolution
chosen here, also when a video is added.

{: .note }
> A slideshow has no sound of its own. Add a [soundtrack]({{ "/operations/soundtracks/" | relative_url }})
> for music; without one the exported video is silent.

Slideshows are free in both editions (4K needs Pro).
