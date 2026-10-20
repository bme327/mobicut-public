---
title: Mute
parent: Operations
nav_order: 7
---

# Mute a segment's sound

Wind noise on the take-off, someone talking behind the camera: mute just that part.

{% include screen.html name="mute" alt="The editor with the middle segment selected, labelled 1× · muted, and the Unmute tool highlighted." %}

1. Select the segment (tap it on the timeline, marker 1). [Split]({{ "/operations/split/" | relative_url }})
   first if only part of it should be silent.
2. Tap **Mute** (marker 2). The segment's label gets **· muted** and turns orange, and the tool
   changes to **Unmute**.

The segment is silent in the preview and in the export. Tap **Unmute** to bring the sound back.

- Muting is separate from speed: segments at **8× and 16×** are muted anyway, whatever this
  setting says.
- [Pictures]({{ "/operations/pictures/" | relative_url }}) have no sound, so **Mute** (like
  **Speed**) is greyed out on them.
- To put music in place of the video's sound, use a
  [soundtrack]({{ "/operations/soundtracks/" | relative_url }}) set to **Replace**.
