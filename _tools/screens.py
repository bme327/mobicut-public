#!/usr/bin/env python3
"""Draws the illustrated phone screens used in the docs.

The screens are drawn from the app's own UI code (colors from ui/Theme.kt, labels from
HomeScreen/EditorScreen/Sheets/TimelineView). They stand in for real screenshots: drop a real
phone screenshot with the same file name into assets/screens/real/ and the pages use it instead
(see _includes/screen.html).

    python3 _tools/screens.py            # writes assets/screens/*.png
Needs: pip install cairosvg ; fonts Inter + DejaVu Sans Mono.
"""
import os
import sys
from html import escape

import cairosvg

# ---- palette (app/src/main/java/app/mobicut/ui/Theme.kt) ----
BG = "#0E0F11"; SURF = "#17191C"; SURF_HI = "#22252A"; SEG = "#2B3036"; OUTLINE = "#2E3238"
TEXT = "#F2F2F0"; MUTED = "#A3A7AE"; ACCENT = "#F2A33A"; ON_ACCENT = "#1A1206"; ACCENT_DIM = "#2A2418"
DEL = "#2A1515"; DEL_LINE = "#C9595A"; DEL_TEXT = "#F3B4B4"; SUB = "#1F3557"; SUB_TEXT = "#BBD3FF"
SND = "#1E4034"; SND_TEXT = "#A8E6C8"; GRAPHIC = "#4A2F57"
CALLOUT = "#3FA9F5"

W, H = 360, 780
VERSION = "2026-10-22.1"  # app release the screens show
SANS = "Inter, sans-serif"; MONO = "DejaVu Sans Mono, monospace"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "screens")


def t(x, y, s, size=14, color=TEXT, weight=400, anchor="start", mono=False, extra=""):
    fam = MONO if mono else SANS
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def rect(x, y, w, h, fill, r=0, stroke=None, sw=1, op=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" fill-opacity="{op}"{s}/>'


# ---- simple icons (24-unit boxes, drawn with strokes) ----
def icon(name, x, y, size=22, color=TEXT):
    k = size / 24
    g = f'<g transform="translate({x - size/2},{y - size/2}) scale({k})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    p = {
        "cut": '<circle cx="6" cy="17" r="3"/><circle cx="6" cy="7" r="3"/><path d="M8.5 15.5 20 5M8.5 8.5 20 19"/>',
        "trash": '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13M10 11v6M14 11v6"/>',
        "restore": '<path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/><path d="M12 17v-5M9.5 14.5 12 12l2.5 2.5"/>',
        "speed": '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-6"/>',
        "subs": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M6 11h4M12 11h6M6 15h8M16 15h2"/>',
        "play": f'<path d="M8 5v14l11-7z" fill="{color}"/>',
        "pause": '<path d="M8 5v14M16 5v14"/>',
        "undo": '<path d="M9 7 4 12l5 5"/><path d="M4 12h11a5 5 0 0 1 0 10h-3"/>',
        "back": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
        "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/>',
        "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/>',
        "plus": '<path d="M12 5v14M5 12h14"/>',
        "more": f'<circle cx="12" cy="5" r="1.6" fill="{color}"/><circle cx="12" cy="12" r="1.6" fill="{color}"/><circle cx="12" cy="19" r="1.6" fill="{color}"/>',
        "movie": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 5v14M17 5v14M3 9h4M3 15h4M17 9h4M17 15h4"/>',
        "gallery": '<rect x="6" y="3" width="15" height="15" rx="2"/><path d="M3 7v12a2 2 0 0 0 2 2h12"/><path d="m9 15 3-4 2 2 2-3 3 5z"/>',
        "folder": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
        "eye_off": '<path d="M3 3l18 18"/><path d="M10.6 6.1A10 10 0 0 1 22 12a14 14 0 0 1-3 3.7M6.6 6.6A14 14 0 0 0 2 12s3.6 7 10 7a9.6 9.6 0 0 0 5.4-1.6"/>',
        "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
        "zoom_in": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21M8 10.5h5M10.5 8v5"/>',
        "zoom_out": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21M8 10.5h5"/>',
        "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
        "video_lib": '<rect x="6" y="3" width="15" height="15" rx="2"/><path d="M3 7v12a2 2 0 0 0 2 2h12"/><path d="m11 7.5 5 3-5 3z"/>',
        "fade": '<path d="M4 12h3l2-5 3 10 3-10 2 5h3"/>',
        "volume": '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11"/>',
        "volume_off": '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M17 9l5 6M22 9l-5 6"/>',
        "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.8"/><path d="m4 18 5-6 4 4 3-3 4 5"/>',
        "skip_prev": '<path d="M6 5v14"/><path d="M18 5 9 12l9 7z"/>',
        "skip_next": '<path d="M18 5v14"/><path d="M6 5l9 7-9 7z"/>',
        "replay5": '<path d="M12 4a8 8 0 1 1-7.6 5.5"/><path d="M4 4v5.5h5.5"/><path d="M10.5 10h3M10.5 10v2.5h1.7a1.6 1.6 0 1 1 0 3.2h-1.7"/>',
        "forward5": '<path d="M12 4a8 8 0 1 0 7.6 5.5"/><path d="M20 4v5.5h-5.5"/><path d="M10.5 10h3M10.5 10v2.5h1.7a1.6 1.6 0 1 1 0 3.2h-1.7"/>',
        "title": '<path d="M5 5h14M12 5v14"/>',
        "category": '<path d="M12 3 7 11h10z"/><circle cx="17" cy="17" r="4"/><rect x="3" y="13" width="8" height="8" rx="1"/>',
        "gradient": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18" stroke-opacity="0.5"/>',
        "gesture": '<path d="M4 15c3-6 5-6 6-3s2 5 4 2 4-7 6-4"/><path d="M15 19h5"/>',
        "link": '<path d="M10 14a4 4 0 0 0 5.6 0l3-3a4 4 0 0 0-5.6-5.6l-1 1"/><path d="M14 10a4 4 0 0 0-5.6 0l-3 3a4 4 0 0 0 5.6 5.6l1-1"/>',
        "music": '<path d="M9 18V6l11-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>',
    }[name]
    return g + p + "</g>"


# ---- video frame: an original paragliding landscape (no real footage) ----
def landscape(x, y, w, h, shade=0, uid="v"):
    sky1, sky2 = ["#5B8FC9", "#9CC3E6"] if shade == 0 else (["#C9785B", "#E6C29C"] if shade == 1 else ["#3E5F86", "#B9D5EC"])
    return (f'<defs><linearGradient id="sky{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky1}"/>'
            f'<stop offset="1" stop-color="{sky2}"/></linearGradient>'
            f'<clipPath id="clip{uid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs>'
            f'<g clip-path="url(#clip{uid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#sky{uid})"/>'
            f'<g transform="translate({x},{y}) scale({w/320},{h/180})">'
            '<path d="M0 120 L60 70 L95 95 L150 45 L205 100 L250 75 L320 115 V180 H0Z" fill="#6C7F93"/>'
            '<path d="M150 45 L165 58 L158 60 L150 52 L140 62 Z" fill="#F4F7FA"/>'
            '<path d="M0 140 L70 110 L130 135 L200 112 L320 140 V180 H0Z" fill="#3F6B4A"/>'
            '<path d="M0 160 L90 148 L170 162 L320 152 V180 H0Z" fill="#2C4E35"/>'
            '<path d="M205 38 Q228 26 252 38" stroke="#E5532F" stroke-width="5" fill="none" stroke-linecap="round"/>'
            '<path d="M207 39 L228 56 M250 39 L228 56" stroke="#20252B" stroke-width="0.8"/>'
            '<circle cx="228" cy="58" r="2.6" fill="#20252B"/></g></g>')


def tile_band(x, y, w, h, deleted=False, uid="t"):
    """Thumbnail tiles inside a segment, like the timeline draws them."""
    out = []
    tw = h * 1.5
    i = 0
    cx = x
    while cx < x + w:
        ww = min(tw, x + w - cx)
        out.append(f'<svg x="{cx}" y="{y}" width="{ww}" height="{h}" viewBox="0 0 {tw} {h}" preserveAspectRatio="xMinYMid slice" opacity="{0.25 if deleted else 0.75}">'
                   + landscape(0, 0, tw, h, shade=i % 3, uid=f"{uid}{i}") + "</svg>")
        cx += tw
        i += 1
    return "".join(out)


def status_bar():
    return (rect(0, 0, W, 24, BG) + t(16, 17, "10:18", 12, TEXT, 500)
            + rect(W - 44, 9, 22, 10, "none", 2, TEXT, 1.2) + rect(W - 42, 11, 14, 6, TEXT, 1)
            + f'<path d="M{W-64} 18 l10 -10 v10z" fill="{TEXT}"/>')


def nav_bar():
    return rect(0, H - 24, W, 24, BG) + rect(W / 2 - 54, H - 14, 108, 4, MUTED, 2)


def scrim():
    return rect(0, 0, W, H, "#000", op=0.55)


def phone(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            + rect(0, 0, W, H, BG) + body + "</svg>")


def callout(n, x, y, tx=None, ty=None, ring=None):
    """Numbered marker; ring=(x,y,w,h) draws a highlight box around a control."""
    s = ""
    if ring:
        rx, ry, rw, rh = ring
        s += rect(rx, ry, rw, rh, "none", 10, CALLOUT, 2.5)
    if tx is not None:
        s += f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{CALLOUT}" stroke-width="2"/>'
    s += f'<circle cx="{x}" cy="{y}" r="11" fill="{CALLOUT}" stroke="{BG}" stroke-width="2"/>'
    s += t(x, y + 4.5, str(n), 12, "#fff", 700, "middle")
    return s


def button(x, y, w, h, label, filled=True, icon_name=None, size=14):
    s = rect(x, y, w, h, ACCENT if filled else "none", h / 2, None if filled else OUTLINE, 1)
    c = ON_ACCENT if filled else ACCENT
    if icon_name:
        tw = len(label) * size * 0.56
        ix = x + w / 2 - tw / 2 - 6
        s += icon(icon_name, ix, y + h / 2, 18, c)
        s += t(ix + 14, y + h / 2 + size * 0.36, label, size, c, 600)
    else:
        s += t(x + w / 2, y + h / 2 + size * 0.36, label, size, c, 600, "middle")
    return s


# ---------------------------------------------------------------- home
def home(projects=True, sheet=False, menu=False):
    s = status_bar()
    s += t(20, 66, "mobiCut", 26, TEXT, 600)
    s += icon("gear", 196, 58, 22, MUTED)
    s += button(222, 36, 124, 44, "New project", icon_name="plus")
    if not projects:
        s += icon("movie", W / 2, 330, 48, ACCENT)
        s += t(W / 2, 382, "No projects yet", 18, TEXT, 600, "middle")
        for i, line in enumerate(["Start one from your gallery, or from a camera’s",
                                  "SD card or USB. Your edits are saved",
                                  "automatically, so you can come back to them here."]):
            s += t(W / 2, 408 + i * 20, line, 13.5, MUTED, 400, "middle")
    else:
        s += t(20, 112, "Recent projects", 13, MUTED)
        rows = [("Lysá hora flight", "3 segments · 2 texts", "Edited 5 minutes ago", "0:48", 0),
                ("Skiing Ramzová", "5 segments", "Edited 2 hours ago", "1:12", 2),
                ("Ondřejník thermals", "1 segment", "Edited yesterday", "3:05", 1)]
        for i, (name, a, b, dur, sh) in enumerate(rows):
            y = 124 + i * 80
            s += f'<svg x="20" y="{y + 8}" width="112" height="63">' + f'<clipPath id="r{i}"><rect width="112" height="63" rx="8"/></clipPath><g clip-path="url(#r{i})">' + landscape(0, 0, 112, 63, sh, f"h{i}") + "</g></svg>"
            s += rect(96, y + 54, 32, 15, "#000", 3, op=0.65) + t(112, y + 65, dur, 11, TEXT, 400, "middle", True)
            s += t(144, y + 30, name, 15, TEXT, 500)
            s += t(144, y + 48, a, 12, MUTED)
            s += t(144, y + 64, b, 12, MUTED)
            s += icon("more", 334, y + 40, 22, MUTED)
        if menu:
            s += rect(196, 176, 150, 104, SURF_HI, 6)
            s += icon("edit", 220, 205, 20, TEXT) + t(242, 210, "Rename", 15)
            s += icon("trash", 220, 252, 20, DEL_LINE) + t(242, 257, "Delete", 15, DEL_LINE)
    s += nav_bar()
    if sheet:
        s += scrim()
        top = H - 230
        s += f'<path d="M0 {top+28} Q0 {top} 28 {top} H{W-28} Q{W} {top} {W} {top+28} V{H} H0Z" fill="{SURF}"/>'
        s += rect(W / 2 - 16, top + 14, 32, 4, MUTED, 2)
        s += t(20, top + 60, "New project from…", 18, TEXT, 600)
        for i, (ic, title, det) in enumerate([("gallery", "Gallery", "Videos on this phone"),
                                              ("folder", "Browse files", "SD card, USB camera or drive, Downloads, Drive")]):
            y = top + 82 + i * 62
            s += icon(ic, 33, y + 24, 26, ACCENT)
            s += t(62, y + 20, title, 16) + t(62, y + 40, det, 13, MUTED)
        s += nav_bar()
    return s


# ---------------------------------------------------------------- editor
DEFAULT_SEGS = [  # (fraction of width, label, speed!=1, deleted, selected)
    (0.36, "1×", False, False, False),
    (0.30, "4×", True, False, True),
    (0.34, "1×", False, False, False),
]


def editor(segs=DEFAULT_SEGS, playhead=0.47, subs=((0.08, 0.30, "Take-off from Lysá hora"), (0.70, 0.93, "Landing")),
           selected_deleted=False, show_deleted=False, transitions=True, transition_set=(), playing=False,
           subtitle_on_preview="", speed_badge="4×", title="Lysá hora flight", time="0:21.4", total="0:48.0",
           video=True, soundtracks=(), preview_shade=0, selected_muted=False, selected_picture=False,
           graphics=((0.40, 0.60, "Arrow"),)):
    """segs: (fraction, label, fast, deleted, selected[, kind[, join_before]]); kind "picture" draws
    a picture segment, join_before draws the white join between two clips instead of a split marker.
    soundtracks: (start fraction, end fraction, name, replace) shown in the lane under subtitles."""
    s = status_bar()
    # header
    s += icon("back", 28, 52, 24, TEXT)
    s += t(56, 49, title, 16, TEXT, 600)
    s += icon("edit", 56 + len(title) * 9.2 + 10, 44, 14, MUTED)
    s += t(56, 66, "1920×1080 · 50 fps · 2:31", 12, MUTED, 400, mono=True)
    s += button(264, 32, 84, 40, "Export")
    # preview
    # The preview gives up room when the soundtrack lane is shown, like the app's weighted layout.
    pv_top, pv_h = 80, 346 - (26 if soundtracks else 0)
    s += rect(0, pv_top, W, pv_h, "#000")
    if video:
        vh = W * 9 / 16
        vy = pv_top + (pv_h - vh) / 2
        s += landscape(0, vy, W, vh, preview_shade, "pv")
        if speed_badge:
            s += rect(10, vy + 10, 36, 20, "#000", 4, op=0.6) + t(28, vy + 24, speed_badge, 12, ACCENT, 600, "middle", True)
        if subtitle_on_preview:
            tw = len(subtitle_on_preview) * 7.6 + 20
            s += rect(W / 2 - tw / 2, vy + vh - 40, tw, 26, "#000", 4, op=0.72)
            s += t(W / 2, vy + vh - 22, subtitle_on_preview, 15, "#fff", 400, "middle")
    # controls
    cy = pv_top + pv_h
    # Transport: to start, −5 s, play/pause, +5 s, to end; then the times, small, on two lines.
    s += icon("skip_prev", 28, cy + 30, 22, TEXT) + icon("replay5", 68, cy + 30, 22, TEXT)
    s += f'<circle cx="110" cy="{cy+30}" r="22" fill="{SURF_HI}"/>' + icon("pause" if playing else "play", 110, cy + 30, 24, TEXT)
    s += icon("forward5", 152, cy + 30, 22, TEXT) + icon("skip_next", 192, cy + 30, 22, TEXT)
    s += t(216, cy + 27, time, 11, TEXT, 400, mono=True) + t(216, cy + 41, total, 11, MUTED, 400, mono=True)
    s += icon("undo", 334, cy + 30, 24, TEXT)
    # timeline
    tl_x, tl_w = 16, 340
    ly = cy + 60 + 12
    for i, lab in enumerate(["0:00", "0:37", "1:15", "1:53", "2:31"]):
        anchor = "start" if i == 0 else ("end" if i == 4 else "middle")
        s += t(tl_x + tl_w * i / 4, ly, lab, 11, MUTED, 400, anchor, True)
    track_top = ly + 4 + 12
    track_h = 84
    x = tl_x
    bounds = []
    joins_at = []
    for i, seg in enumerate(segs):
        frac, lab, fast, deleted, sel = seg[:5]
        kind = seg[5] if len(seg) > 5 else None
        join_before = seg[6] if len(seg) > 6 else False
        w = tl_w * frac
        left = x + (1 if i > 0 else 0)
        right = x + w - (1 if i < len(segs) - 1 else 0)
        s += f'<clipPath id="sg{i}"><rect x="{left}" y="{track_top}" width="{right-left}" height="{track_h}" rx="6"/></clipPath><g clip-path="url(#sg{i})">'
        s += rect(left, track_top, right - left, track_h, SEG)
        if video and kind == "picture":
            s += (f'<svg x="{left}" y="{track_top}" width="{right-left}" height="{track_h}" viewBox="0 0 {track_h*1.5} {track_h}" '
                  f'preserveAspectRatio="xMinYMid slice" opacity="0.8">' + landscape(0, 0, track_h * 1.5, track_h, 1, f"pic{i}") + "</svg>")
        elif video:
            s += tile_band(left, track_top, right - left, track_h, deleted, f"tb{i}")
        if deleted:
            s += rect(left, track_top, right - left, track_h, DEL, op=0.7)
            hx = left - track_h
            while hx < right:
                s += f'<line x1="{hx}" y1="{track_top+track_h}" x2="{hx+track_h}" y2="{track_top}" stroke="{DEL_LINE}" stroke-opacity="0.45" stroke-width="1.5"/>'
                hx += 10
        s += "</g>"
        stroke = ACCENT if sel else (DEL_LINE if deleted else None)
        if stroke:
            s += rect(left, track_top, right - left, track_h, "none", 6, stroke, 2.5 if sel else 1)
        label = "Deleted" if deleted else lab
        col = DEL_TEXT if deleted else (ACCENT if (sel or fast) else TEXT)
        lw = len(label) * 7.2 + 6
        s += rect(left + 3, track_top + track_h - 24, lw, 18, "#000", 3, op=0.55)
        s += t(left + 6, track_top + track_h - 11, label, 12, col, 500, mono=True)
        if sel:
            s += f'<circle cx="{right-20}" cy="{track_top+20}" r="12" fill="#000" fill-opacity="0.6"/>' + icon("info", right - 20, track_top + 20, 18, TEXT)
        if i > 0:
            (joins_at if join_before else bounds).append(x)
        x += w
    for bx in bounds:
        s += f'<line x1="{bx}" y1="{track_top-2}" x2="{bx}" y2="{track_top+track_h}" stroke="{ACCENT}" stroke-width="2"/>'
        s += f'<path d="M{bx-6} {track_top-12} H{bx+6} L{bx} {track_top-1}Z" fill="{ACCENT}"/>'
    for jx in joins_at:
        s += f'<line x1="{jx}" y1="{track_top}" x2="{jx}" y2="{track_top+track_h}" stroke="#fff" stroke-opacity="0.85" stroke-width="3"/>'
    if transitions and not show_deleted:
        joins = [tl_x] + sorted(bounds + joins_at) + [tl_x + tl_w]
        for j, jx in enumerate(joins):
            cxp = min(max(jx, tl_x + 18), tl_x + tl_w - 18)
            on = j in transition_set
            s += f'<circle cx="{cxp}" cy="{track_top+track_h/2}" r="13" fill="{ACCENT if on else "#000"}" fill-opacity="{1 if on else 0.65}"/>'
            s += icon("fade", cxp, track_top + track_h / 2, 16, ON_ACCENT if on else TEXT)
    px = tl_x + tl_w * playhead
    s += f'<line x1="{px}" y1="{track_top-4}" x2="{px}" y2="{track_top+track_h}" stroke="#fff" stroke-width="2"/><circle cx="{px}" cy="{track_top-4}" r="5" fill="#fff"/>'
    # subtitles
    sy = track_top + track_h + 6
    if not subs:
        s += t(tl_x, sy + 18, "Texts and graphics appear here", 11, MUTED, extra='fill-opacity="0.6"')
    for a, b, txt in subs:
        s += f'<clipPath id="st{a}"><rect x="{tl_x+tl_w*a}" y="{sy}" width="{tl_w*(b-a)}" height="28" rx="5"/></clipPath>'
        s += rect(tl_x + tl_w * a, sy, tl_w * (b - a), 28, SUB, 5)
        s += f'<g clip-path="url(#st{a})">' + icon("title", tl_x + tl_w * a + 9, sy + 14, 12, SUB_TEXT + "BF")
        s += t(tl_x + tl_w * a + 18, sy + 18, txt, 11, SUB_TEXT) + "</g>"
    for a, b, txt in (graphics if subs else ()):
        s += f'<clipPath id="gr{a}"><rect x="{tl_x+tl_w*a}" y="{sy}" width="{tl_w*(b-a)}" height="28" rx="5"/></clipPath>'
        s += rect(tl_x + tl_w * a, sy, tl_w * (b - a), 28, GRAPHIC, 5)
        s += f'<g clip-path="url(#gr{a})">' + icon("category", tl_x + tl_w * a + 10, sy + 14, 12, SUB_TEXT + "BF")
        s += t(tl_x + tl_w * a + 20, sy + 18, txt, 11, SUB_TEXT) + "</g>"
    # soundtrack lane
    if soundtracks:
        ly2 = sy + 32
        for a, b, name, replace in soundtracks:
            x0, x1 = tl_x + tl_w * a, tl_x + tl_w * b
            s += f'<clipPath id="snd{a}"><rect x="{x0}" y="{ly2}" width="{x1-x0}" height="22" rx="4"/></clipPath>'
            s += rect(x0, ly2, x1 - x0, 22, SND, 4)
            s += f'<g clip-path="url(#snd{a})">' + t(x0 + 6, ly2 + 15, ("♪ only · " if replace else "♪ ") + name, 10, SND_TEXT).replace(SANS, "DejaVu Sans, sans-serif") + "</g>"
        sy += 26
    # zoom row
    zy = sy + 28 + 26
    s += icon("eye" if show_deleted else "eye_off", 40, zy, 22, DEL_TEXT if show_deleted else MUTED)
    s += icon("zoom_out", 86, zy, 22, MUTED + "66")
    s += rect(112, zy - 2, 196, 4, SURF, 2) + f'<circle cx="120" cy="{zy}" r="8" fill="{MUTED}" fill-opacity="0.4"/>'
    s += icon("zoom_in", 332, zy, 22, TEXT)
    # toolbar
    ty = H - 24 - 76
    dim = MUTED + "66"
    tools = [("cut", "Split", TEXT), ("restore" if selected_deleted else "trash", "Restore" if selected_deleted else "Delete", TEXT),
             ("speed", "Speed", dim if selected_picture else TEXT),
             ("volume_off" if selected_muted else "volume", "Unmute" if selected_muted else "Mute",
              dim if selected_picture else (ACCENT if selected_muted else TEXT)),
             ("subs", "Text", TEXT), ("category", "Graphic", TEXT), ("plus", "Add", TEXT)]
    for i, (ic, lab, col) in enumerate(tools):
        bx = TOOL_X[i]
        s += icon(ic, bx, ty + 28, 22, col) + t(bx, ty + 56, lab, 12, col, 400, "middle")
    s += nav_bar()
    return s


TOOL_W = (W - 8) / 7
TOOL_X = [4 + TOOL_W * i + TOOL_W / 2 for i in range(7)]
TOOL_Y = H - 24 - 76


def tool_ring(i):
    return (TOOL_X[i] - 25, TOOL_Y + 6, 50, 62)


# ---------------------------------------------------------------- overlays
def sheet(height, content):
    top = H - height
    s = scrim()
    s += f'<path d="M0 {top+28} Q0 {top} 28 {top} H{W-28} Q{W} {top} {W} {top+28} V{H} H0Z" fill="{SURF}"/>'
    s += rect(W / 2 - 16, top + 14, 32, 4, MUTED, 2)
    return s + content(top) + nav_bar()


def dialog(height, title, body, buttons, width=312):
    x = (W - width) / 2
    y = (H - height) / 2
    s = scrim() + rect(x, y, width, height, SURF_HI, 28)
    s += t(x + 24, y + 44, title, 22, TEXT, 400)
    s += body(x + 24, y + 70, width - 48)
    bx = x + width - 24
    for lab, col in reversed(buttons):
        w = len(lab) * 8.2 + 24
        s += t(bx - w / 2, y + height - 28, lab, 14, col, 600, "middle")
        bx -= w + 8
    return s


def radio(x, y, on):
    s = f'<circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{ACCENT if on else MUTED}" stroke-width="2"/>'
    if on:
        s += f'<circle cx="{x}" cy="{y}" r="5" fill="{ACCENT}"/>'
    return s


def stepper(x, y, value):
    s = rect(x, y, 40, 40, "none", 20, OUTLINE, 1) + t(x + 20, y + 27, "−", 20, ACCENT, 400, "middle")
    s += t(x + 68, y + 26, value, 15, TEXT, 400, "middle", True)
    s += rect(x + 96, y, 40, 40, "none", 20, OUTLINE, 1) + t(x + 116, y + 27, "+", 20, ACCENT, 400, "middle")
    return s


def speed_sheet():
    def c(top):
        s = t(16, top + 52, "Segment speed", 18, TEXT, 600)
        s += t(16, top + 72, "0:54.1 – 1:31.5 · source 0:37.4", 12, MUTED, 400, mono=True)
        s += t(W - 16, top + 60, "0:09.3", 22, ACCENT, 400, "end", True) + t(W - 16, top + 78, "in output", 12, MUTED, 400, "end")
        speeds = ["0.25×", "0.5×", "1×", "2×", "4×", "8×", "16×"]
        cw = (W - 32 - 24) / 4
        for i, sp in enumerate(speeds):
            r, col = divmod(i, 4)
            x = 16 + col * (cw + 8)
            y = top + 98 + r * 56
            sel = sp == "4×"
            s += rect(x, y, cw, 48, ACCENT_DIM if sel else SURF_HI, 10, ACCENT if sel else OUTLINE, 2 if sel else 1)
            s += t(x + cw / 2, y + 29, sp, 15, ACCENT if sel else TEXT, 400, "middle", True)
        s += t(16, top + 228, "Audio keeps its natural pitch. It's muted", 12, MUTED) + t(16, top + 244, "automatically at 8× and above.", 12, MUTED)
        s += button(16, top + 256, W - 32, 48, "Done")
        return s
    return editor() + sheet(350, c)


def export_sheet():
    def c(top):
        s = t(16, top + 52, "Export", 18, TEXT, 600)
        s += t(16, top + 76, "Length 0:48.0 · 3 segments", 13, MUTED, 400, mono=True)
        y = top + 104
        for title, opts, sel in [("Resolution", ["Original", "720p"], 0),
                                 ("Frame rate", ["Original · 50 fps", "30 fps"], 0),
                                 ("Text", ["Burn into video", "Off"], 0)]:
            s += t(16, y, title, 13, MUTED)
            y += 8
            for i, o in enumerate(opts):
                s += radio(28, y + 22, i == sel) + t(48, y + 27, o, 15)
                y += 42
            y += 14
        s += t(16, y - 4, "If this phone can't encode the original settings,", 12, MUTED) + t(16, y + 12, "export steps down automatically.", 12, MUTED)
        s += button(16, y + 20, W - 32, 52, "Export to gallery", size=15)
        return s
    return editor() + sheet(600, c)


def export_done():
    def body(x, y, w):
        return t(x, y + 10, "Movies/MobiCut", 14, MUTED)
    return editor() + dialog(170, "Saved to gallery", body, [("Share", ACCENT), ("Close", ACCENT), ("Play", ACCENT)])


def export_running():
    def body(x, y, w):
        return rect(x, y + 4, w, 4, SURF, 2) + rect(x, y + 4, w * 0.42, 4, ACCENT, 2) + t(x, y + 34, "42 %  ·  keep MobiCut open", 13, MUTED)
    return editor() + dialog(180, "Exporting…", body, [("Cancel", ACCENT)])


def transition_dialog():
    def body(x, y, w):
        s = t(x, y + 6, "Type", 13, MUTED)
        s += radio(x + 10, y + 32, True) + t(x + 30, y + 30, "Fade out-in", 15) + t(x + 30, y + 46, "Dips to black and back", 12, MUTED)
        s += radio(x + 10, y + 80, False) + t(x + 30, y + 78, "Interleave", 15) + rect(x + 112, y + 66, 34, 15, ACCENT, 7) + t(x + 129, y + 77, "PRO", 9, ON_ACCENT, 900, "middle") + t(x + 30, y + 94, "Crossfade. The video gets shorter", 12, MUTED) + t(x + 30, y + 109, "by the duration", 12, MUTED)
        s += t(x, y + 148, "Duration", 14) + t(x, y + 165, "Total, in", 12, MUTED) + t(x, y + 180, "the export", 12, MUTED)
        s += stepper(x + w - 136, y + 134, "1.0 s")
        return s
    return editor(transition_set=(1,)) + dialog(350, "Add transition", body, [("Cancel", ACCENT), ("Save & play", ACCENT), ("Save", ACCENT)])


def segment_info():
    def body(x, y, w):
        rows = [("In the video", "0:54.1 – 1:31.5"), ("Length", "37.4 s"), ("Speed", "4×"),
                ("In the export", "0:54.1 – 1:03.4"), ("Export length", "9.3 s"), ("Audio", "On, natural pitch")]
        s = ""
        for i, (a, b) in enumerate(rows):
            s += t(x, y + 6 + i * 30, a, 14, MUTED) + t(x + w, y + 6 + i * 30, b, 14, TEXT, 400, "end", True)
        return s
    return editor() + dialog(330, "Segment 2 of 3", body, [("Close", ACCENT)])


def missing_video():
    s = editor(video=False, speed_badge="")
    # replace the black preview with the "can't find" panel
    s += rect(0, 80, W, 346, SURF)
    s += icon("video_lib", W / 2, 170, 40, ACCENT)
    s += t(W / 2, 214, "Can't find this project's video", 16, TEXT, 600, "middle")
    for i, line in enumerate(["It may have been moved, deleted, or on a card or",
                              "camera that is unplugged. Your edits are safe.",
                              "Pick the same video to continue."]):
        s += t(W / 2, 240 + i * 19, line, 13.5, MUTED, 400, "middle")
    s += button(W / 2 - 132, 312, 110, 44, "Gallery") + button(W / 2 - 10, 312, 142, 44, "Browse files", filled=False)
    return s


def rename_dialog():
    def body(x, y, w):
        return (rect(x, y, w, 56, "none", 4, ACCENT, 2) + rect(x + 14, y + 16, 168, 24, ACCENT, op=0.35)
                + t(x + 16, y + 33, "Lysá hora flight", 16))
    return home() + dialog(220, "Rename project", body, [("Cancel", ACCENT), ("Rename", ACCENT)])


def delete_project_dialog():
    def body(x, y, w):
        lines = ["\"Lysá hora flight\" and its edits will be", "removed. The original video and any", "exports stay in your gallery."]
        return "".join(t(x, y + 6 + i * 20, l, 14, MUTED) for i, l in enumerate(lines))
    return home() + dialog(220, "Delete project?", body, [("Cancel", ACCENT), ("Delete", DEL_LINE)])


def settings_sheet():
    def c(top):
        s = t(20, top + 52, "Settings", 18, TEXT, 600)
        s += t(20, top + 90, "Edition", 15) + rect(W - 66, top + 76, 46, 18, ACCENT, 9) + t(W - 43, top + 89, "PRO", 10, ON_ACCENT, 900, "middle")
        y = top + 112
        s += rect(20, y, W - 40, 124, "none", 12, OUTLINE, 1)
        s += t(34, y + 26, "Test build: edition", 13, TEXT, 600)
        s += rect(34, y + 40, 62, 32, "none", 8, OUTLINE, 1) + t(65, y + 61, "Free", 14, TEXT, 500, "middle")
        s += rect(104, y + 40, 58, 32, ACCENT, 8) + t(133, y + 61, "Pro", 14, ON_ACCENT, 600, "middle")
        s += t(34, y + 92, "Only in test builds. The Play Store version takes", 12, MUTED)
        s += t(34, y + 108, "the edition from your Google Play purchase.", 12, MUTED)
        s += t(20, y + 156, "Privacy policy", 15, ACCENT)
        s += t(20, y + 184, f"mobiCut {VERSION}", 12, MUTED)
        return s
    return home() + sheet(352, c)


def add_sheet():
    def c(top):
        s = t(16, top + 52, "Add", 18, TEXT, 600)
        rows = [("title", "Text slide at the pointer", "A title card from a template, split into the video"),
                ("image", "Picture at the pointer", "A still or moving picture, split into the video"),
                ("music", "Soundtrack at the pointer", "Music or any audio file, under the video"),
                ("gradient", "Transitions at every join", "One transition everywhere, plus fade in and out"),
                ("video_lib", "Video from Gallery", "Added at the end of the timeline"),
                ("video_lib", "Video from files", "SD card, USB, Downloads, Drive…")]
        for i, (ic, title, det) in enumerate(rows):
            y = top + 74 + i * 60
            s += icon(ic, 32, y + 24, 24, ACCENT)
            s += t(60, y + 20, title, 15) + t(60, y + 40, det, 12, MUTED)
        # Videos are Pro: the badge sits on their group.
        s += rect(W - 62, top + 74 + 4 * 60 + 2, 46, 18, ACCENT, 9) + t(W - 39, top + 74 + 4 * 60 + 15, "PRO", 10, ON_ACCENT, 900, "middle")
        return s
    return editor() + sheet(460, c)


MEDIA_SEGS = [  # first video, a picture, the first video again, a second video
    (0.26, "1×", False, False, False),
    (0.18, "Zoom in", False, False, True, "picture", True),
    (0.28, "1× · muted", False, False, False, None, True),
    (0.28, "1×", False, False, False, None, True),
]


def picture_dialog():
    def body(x, y, w):
        s = button(x, y, 96, 40, "Gallery") + button(x + 106, y, 124, 40, "Browse files", filled=False)
        s += t(x, y + 64, "Ramzová summit.jpg", 13, TEXT)
        s += t(x, y + 100, "Duration", 14) + t(x, y + 117, "How long it shows,", 12, MUTED) + t(x, y + 132, "before transitions", 12, MUTED)
        s += stepper(x + w - 136, y + 88, "3.0 s")
        s += t(x, y + 170, "Effect", 13, MUTED)
        opts = [("Still", "No movement"), ("Slow zoom in", "Moves closer over the whole duration"),
                ("Slow zoom out", "Starts close, moves back"), ("Slide in", "Comes in from the right, then stays")]
        for i, (a, b) in enumerate(opts):
            oy = y + 196 + i * 44
            s += radio(x + 10, oy + 6, i == 1) + t(x + 30, oy + 4, a, 15) + t(x + 30, oy + 20, b, 12, MUTED)
        s += t(x, y + 392, "Transitions work as for any segment: use", 12, MUTED) + t(x, y + 408, "the buttons on the timeline.", 12, MUTED)
        return s
    return editor(segs=MEDIA_SEGS, speed_badge="", preview_shade=1) + dialog(560, "Add picture", body, [("Cancel", ACCENT), ("Insert", ACCENT)])


def soundtrack_dialog():
    def body(x, y, w):
        s = t(x, y, "Starts at 0:04.0 in the export · plays 0:44.0", 12, MUTED) + t(x, y + 16, "(cut at the end of the video)", 12, MUTED)
        s += t(x, y + 46, "Start at the pointer (0:21.4)", 14, ACCENT, 600)
        s += t(x, y + 80, "Sound", 13, MUTED)
        s += radio(x + 10, y + 104, False) + t(x + 30, y + 102, "Mix", 15) + t(x + 30, y + 118, "Together with the video's own sound", 12, MUTED)
        s += radio(x + 10, y + 148, True) + t(x + 30, y + 146, "Replace", 15) + t(x + 30, y + 162, "Mutes the video's sound while this plays", 12, MUTED)
        s += t(x, y + 200, "Volume", 14) + t(x + w, y + 200, "80 %", 14, TEXT, 400, "end", True)
        s += rect(x, y + 214, w, 4, SURF, 2) + rect(x, y + 214, w * 0.8, 4, ACCENT, 2) + f'<circle cx="{x + w * 0.8}" cy="{y + 216}" r="9" fill="{ACCENT}"/>'
        s += t(x, y + 262, "Fade in", 14) + stepper(x + w - 136, y + 240, "2.0 s")
        s += t(x, y + 312, "Fade out", 14) + stepper(x + w - 136, y + 290, "3.0 s")
        s += t(x, y + 362, "Remove soundtrack", 14, DEL_LINE, 600)
        return s
    ed = editor(segs=MEDIA_SEGS, speed_badge="", soundtracks=((0.08, 1.0, "Sunrise over the ridge", True),))
    return ed + dialog(560, "Sunrise over the ridge", body, [("Cancel", ACCENT), ("Save", ACCENT)])


def segment_info_picture():
    def body(x, y, w):
        rows = [("Picture", "Ramzová summit"), ("Shown", "0:00.0 – 0:03.0"), ("Length", "3.0 s"), ("Effect", "Zoom in"),
                ("In the export", "0:14.2 – 0:17.2"), ("Export length", "3.0 s")]
        s = ""
        for i, (a, b) in enumerate(rows):
            s += t(x, y + 6 + i * 30, a, 14, MUTED) + t(x + w, y + 6 + i * 30, b, 14, TEXT, 400, "end", True)
        s += t(x, y + 196, "Duration & effect…", 14, ACCENT, 600)
        s += t(x, y + 232, "Remove this picture", 14, DEL_LINE, 600)
        return s
    return editor(segs=MEDIA_SEGS, speed_badge="", preview_shade=1, selected_picture=True) + dialog(380, "Segment 2 of 4", body, [("Close", ACCENT)])


# ---------------------------------------------------------------- screens with callouts
SPLIT_SEGS = [(0.47, "1×", False, False, False), (0.53, "1×", False, False, True)]
DEL_SEGS = [(0.36, "1×", False, False, False), (0.30, "4×", True, True, True), (0.34, "1×", False, False, False)]
TL_TRACK_TOP = 80 + 346 + 60 + 12 + 16

# ---------------------------------------------------------------- subtitle editor (ui/OverlayEditor.kt)
PANEL_TOP = H - 24 - 404   # the panel replaces controls, timeline and toolbar; the preview shrinks
SUB_VY = 80 + (PANEL_TOP - 80 - W * 9 / 16) / 2
SUB_BOX = (0.08, 0.78, 0.84, 0.13)  # x, y, w, h as fractions of the video frame


def chip(x, y, label, sel=False, font=SANS):
    w = len(label) * 7.4 + 26
    s = rect(x, y, w, 32, ACCENT_DIM if sel else "none", 8, None if sel else OUTLINE, 1)
    s += f'<text x="{x + w / 2}" y="{y + 21}" font-family="{font}" font-size="13" fill="{ACCENT if sel else TEXT}" text-anchor="middle">{escape(label)}</text>'
    return s, w


def chips(x, y, labels, selected=(), fonts=None):
    s = ""
    for i, lab in enumerate(labels):
        c, w = chip(x, y, lab, lab in selected, (fonts or {}).get(lab, SANS))
        s += c
        x += w + 8
    return s


def slider(y, label, value, frac):
    s = t(16, y, label, 13, MUTED) + t(W - 16, y, value, 13, TEXT, 400, "end", True)
    s += rect(16, y + 16, W - 32, 4, SURF_HI, 2) + rect(16, y + 16, (W - 32) * frac, 4, ACCENT, 2)
    s += f'<circle cx="{16 + (W - 32) * frac}" cy="{y + 18}" r="9" fill="{ACCENT}"/>'
    return s


def outline_button(x, y, w, h, label, icon_name=None):
    s = rect(x, y, w, h, "none", h / 2, OUTLINE, 1)
    if icon_name:
        s += icon(icon_name, x + 20, y + h / 2, 18, ACCENT)
        return s + t(x + 36, y + h / 2 + 5, label, 14, ACCENT, 500)
    return s + t(x + w / 2, y + h / 2 + 5, label, 14, ACCENT, 500, "middle")


def rotate_handle(cx, top):
    """The round handle on a stalk above an overlay's box (OverlayLayer)."""
    return (f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{top - 22}" stroke="{ACCENT}" stroke-width="1.5"/>'
            f'<circle cx="{cx}" cy="{top - 30}" r="9" fill="#fff"/><circle cx="{cx}" cy="{top - 30}" r="7" fill="{ACCENT}"/>'
            f'<path d="M{cx-3.5} {top-31} a3.5 3.5 0 1 1 1 2.6" fill="none" stroke="{ON_ACCENT}" stroke-width="1.4"/>')


def path_curve(vy, vh, ex, ey):
    """A faint captured path across the video, ending near (ex, ey)."""
    sx, sy = W * 0.12, vy + vh * 0.25
    return (f'<path d="M{sx} {sy} C{W*0.35} {vy+vh*0.05}, {W*0.45} {vy+vh*0.7}, {ex} {ey} S{W*0.85} {vy+vh*0.4}, {W*0.9} {vy+vh*0.3}" '
            f'fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="2" stroke-dasharray="2 5" stroke-linecap="round"/>')


def subtitle_editor(tab="Text", text="Take-off from Lysá hora", look="classic"):
    s = status_bar()
    s += icon("back", 28, 52, 24, TEXT) + t(56, 49, "Lysá hora flight", 16, TEXT, 600)
    s += t(56, 66, "1920×1080 · 50 fps · 2:31", 12, MUTED, 400, mono=True) + button(264, 32, 84, 40, "Export")
    # preview with the subtitle drawn on the video, box and corner handles
    vh = W * 9 / 16
    s += rect(0, 80, W, PANEL_TOP - 80, "#000") + landscape(0, SUB_VY, W, vh, 0, "se")
    bx, by, bw, bh = SUB_BOX
    x0, y0, w0, h0 = bx * W, SUB_VY + by * vh, bw * W, bh * vh
    if look == "classic":
        s += rect(x0, y0, w0, h0, "#000", 4, op=0.72) + t(W / 2, y0 + h0 / 2 + 4.5, text, 13, "#fff", 400, "middle")
    else:  # bold serif, yellow, no background: a soft shadow keeps it readable
        s += t(W / 2 + 1, y0 + h0 / 2 + 7, text, 19, "#000", 700, "middle", extra='fill-opacity="0.6" font-family="DejaVu Serif, serif"').replace(f'font-family="{SANS}" ', "")
        s += t(W / 2, y0 + h0 / 2 + 6, text, 19, "#FFEB3B", 700, "middle", extra='font-family="DejaVu Serif, serif"').replace(f'font-family="{SANS}" ', "")
    s += f'<rect x="{x0}" y="{y0}" width="{w0}" height="{h0}" fill="none" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="5 4"/>'
    for cx, cy in ((x0, y0), (x0 + w0, y0), (x0, y0 + h0), (x0 + w0, y0 + h0)):
        s += f'<circle cx="{cx}" cy="{cy}" r="8.5" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="7" fill="{ACCENT}"/>'
    s += rotate_handle(x0 + w0 / 2, y0)
    if tab == "Path":  # the saved path, faint, through the box centre
        s += path_curve(SUB_VY, vh, x0 + w0 / 2, y0 + h0 / 2)
    # panel
    top = PANEL_TOP
    s += rect(0, top, W, H - top, SURF)
    s += t(16, top + 30, "Text", 16, TEXT, 600)
    s += icon("play", 238, top + 24, 24, TEXT) + icon("trash", 280, top + 24, 22, DEL_LINE)
    s += button(300, top + 6, 52, 36, "Done")
    tw = (W - 16) / 3
    for i, lab in enumerate(["Text", "Look", "Motion"]):
        sel = lab == tab or (lab == "Motion" and tab == "Path")
        cx = 8 + tw * i + tw / 2
        s += t(cx, top + 68, lab, 14, ACCENT if sel else MUTED, 600 if sel else 400, "middle")
        s += rect(8 + tw * i, top + 80, tw, 2, ACCENT if sel else OUTLINE)
    y = top + 98
    if tab == "Text":
        s += rect(16, y, W - 32, 56, "none", 4, MUTED, 1) + t(32, y + 33, text, 16)
        s += t(16, y + 86, "Duration", 14) + t(16, y + 103, "On screen in the export", 12, MUTED)
        s += stepper(W - 16 - 136, y + 72, "5.0 s")
        s += t(16, y + 144, "Starts at", 14)
        bxs = 16
        for lab in ["−1 s", "−0.1"]:
            w = len(lab) * 7.5 + 18
            s += rect(bxs, y + 154, w, 38, "none", 19, OUTLINE, 1) + t(bxs + w / 2, y + 178, lab, 13, ACCENT, 600, "middle")
            bxs += w + 6
        s += t(W / 2, y + 178, "0:12.0", 16, TEXT, 400, "middle", True)
        bxe = W - 16
        for lab in ["+1 s", "+0.1"]:
            w = len(lab) * 7.5 + 18
            bxe -= w
            s += rect(bxe, y + 154, w, 38, "none", 19, OUTLINE, 1) + t(bxe + w / 2, y + 178, lab, 13, ACCENT, 600, "middle")
            bxe -= 6
        s += t(16, y + 212, "Or drag the text along the timeline", 12, MUTED)
    elif tab == "Look":
        s += t(16, y, "Font", 13, MUTED)
        s += chips(16, y + 10, ["Sans", "Serif", "Mono", "Condensed", "Casual"], ("Serif",),
                   {"Serif": "DejaVu Serif, serif", "Mono": MONO})
        s += chips(16, y + 52, ["Bold", "Italic"], ("Bold",))
        for i, (ax, sel) in enumerate(((0, False), (1, True), (2, False))):
            cx = 190 + i * 44
            col = ACCENT if sel else MUTED
            lines = [(-7, 7), (-5, 5) if ax == 1 else ((-7, 3) if ax == 0 else (-3, 7)), (-7, 7), (-5, 5) if ax == 1 else ((-7, 3) if ax == 0 else (-3, 7))]
            for j, (a, b) in enumerate(lines):
                s += f'<line x1="{cx + a}" y1="{y + 60 + j * 5}" x2="{cx + b}" y2="{y + 60 + j * 5}" stroke="{col}" stroke-width="2" stroke-linecap="round"/>'
        s += slider(y + 112, "Size", "7.0 %", (7 - 2) / 14)
        s += t(16, y + 160, "Text colour", 13, MUTED)
        sw = ["#FFFFFF", "#000000", "#FFEB3B", "#F2A33A", "#E53935", "#43A047", "#00BCD4", "#1E88E5", "#D81B60"]
        for i, c in enumerate(sw):
            cx = 32 + i * 42
            sel = c == "#FFEB3B"
            s += f'<circle cx="{cx}" cy="{y + 188}" r="16" fill="none" stroke="{ACCENT if sel else OUTLINE}" stroke-width="{3 if sel else 1}"/>'
            s += f'<circle cx="{cx}" cy="{y + 188}" r="{11 if sel else 13}" fill="{c}"/>'
        s += slider(y + 228, "Text opacity", "100 %", 1.0)
        s += t(16, y + 274, "Background colour", 13, MUTED)  # …and its opacity below, when scrolled
    elif tab == "Path":  # the Motion tab scrolled down, after a capture
        s += t(16, y, "Effect while shown", 13, MUTED) + chips(16, y + 10, ["None", "Wobble", "Pulse", "Shake", "Float"], ("None",))
        s += rect(16, y + 62, W - 32, 1, OUTLINE)
        s += t(16, y + 96, "Path: 5.0 s recorded", 14) + icon("play", W - 36, y + 91, 24, TEXT)
        s += outline_button(16, y + 116, 112, 40, "Clear path") + outline_button(136, y + 116, 136, 40, "Capture again")
        s += outline_button(16, y + 168, 176, 40, "Follow path from…", "link")
    else:
        s += t(16, y, "Ease in", 13, MUTED) + chips(16, y + 10, ["None", "Fade", "Slide", "Zoom", "Type"], ("Zoom",))
        s += slider(y + 66, "Duration", "0.4 s", (0.4 - 0.1) / 1.9)
        s += t(16, y + 116, "Ease out", 13, MUTED) + chips(16, y + 126, ["None", "Fade", "Slide", "Zoom", "Type"], ("Fade",))
        s += slider(y + 182, "Duration", "0.3 s", (0.3 - 0.1) / 1.9)
        s += t(16, y + 232, "Effect while shown", 13, MUTED) + chips(16, y + 242, ["None", "Wobble", "Pulse", "Shake", "Float"], ("Wobble",))
        s += t(16, y + 298, "Tap ▶ above to see it move.", 12, MUTED).replace(SANS, "DejaVu Sans, sans-serif")
    s += nav_bar()
    return s


SUB_BOX_PX = (SUB_BOX[0] * W, SUB_VY + SUB_BOX[1] * W * 9 / 16, SUB_BOX[2] * W, SUB_BOX[3] * W * 9 / 16)

MEDIA_TOP = TL_TRACK_TOP - 26  # timeline moves up when the soundtrack lane is shown

# ---------------------------------------------------------------- welcome (ui/StartupScreen.kt)
def logo(cx, cy, width):
    """The (mc) disc + "mobiCut" wordmark, sized like Logo(): disc 1.25 em, gap 0.3 em."""
    font = width / (1.25 + 0.3 + 3.6)
    disc = font * 1.25
    x0 = cx - width / 2
    s = f'<circle cx="{x0 + disc / 2}" cy="{cy}" r="{disc / 2}" fill="{ACCENT}"/>'
    s += t(x0 + disc / 2, cy + font * 0.22, "mc", font * 0.62, ON_ACCENT, 700, "middle", extra='letter-spacing="-1"')
    s += (f'<text x="{x0 + disc + font * 0.3}" y="{cy + font * 0.36}" font-family="{SANS}" font-size="{font}" fill="{TEXT}">'
          f'mobi<tspan font-weight="700">Cut</tspan></text>')
    return s


def welcome(held=False, fill=0.4):
    s = status_bar()
    s += logo(W / 2, 150, W * 0.7)
    s += t(W / 2, 352, "Quick cuts, speed-ups and text for your action", 15, TEXT, 400, "middle")
    s += t(W / 2, 374, "clips, right on the phone.", 15, TEXT, 400, "middle")
    s += t(W / 2, 404, f"by Ondřej Spilka · version {VERSION}", 12.5, MUTED, 400, "middle")
    s += t(W / 2 - 92, 442, "Docs", 14, ACCENT, 500, "middle") + t(W / 2, 442, "What's new", 14, ACCENT, 500, "middle")
    s += t(W / 2 + 92, 442, "Privacy", 14, ACCENT, 500, "middle")
    s += t(W / 2, 486, "Free edition", 13, MUTED, 400, "middle")
    s += button(W / 2 - 56, 500, 112, 40, "Upgrade")
    y = 690
    s += rect(20, y, 98, 48, "none", 24, OUTLINE, 1) + t(69, y + 29, "Held" if held else "Hold…", 15, TEXT if held else MUTED, 400, "middle")
    bx, bw = 128, W - 148
    s += rect(bx, y, bw, 48, ACCENT_DIM, 24)
    label = "Straight to app" if held else "Straight to app · 3"
    if not held and fill > 0:
        s += f'<clipPath id="cd"><rect x="{bx}" y="{y}" width="{bw * fill}" height="48"/></clipPath>'
        s += f'<g clip-path="url(#cd)">' + rect(bx, y, bw, 48, ACCENT, 24) + "</g>"
    s += t(bx + bw / 2, y + 29, label, 15, ACCENT, 600, "middle")
    if not held and fill > 0:
        s += f'<g clip-path="url(#cd)">' + t(bx + bw / 2, y + 29, label, 15, ON_ACCENT, 600, "middle") + "</g>"
    return s + nav_bar()


# ---------------------------------------------------------------- graphics (model/Graphic.kt, export/ShapeArt.kt)
YELLOW = "#FFD54F"; RED = "#E53935"


def shape_art(name, cx, cy, size, line=RED, fill=None, lw=None):
    """Simple stand-ins for ShapeArt: drawn into a size×size box centred on (cx, cy)."""
    r = size / 2
    lw = lw or max(2, size / 14)
    x0, y0 = cx - r, cy - r
    fl = f'fill="{fill}" fill-opacity="0.35"' if fill else 'fill="none"'
    st = f'stroke="{line}" stroke-width="{lw}" stroke-linecap="round" stroke-linejoin="round"'
    sl = 'fill="none" ' + st
    if name.startswith("smiley"):
        mood = name.split("_")[1]
        s = f'<circle cx="{cx}" cy="{cy}" r="{r*0.9}" fill="{YELLOW}" stroke="#5D4037" stroke-width="{lw*0.7}"/>'
        ey = cy - r * 0.2
        if mood == "wink":
            s += f'<circle cx="{cx-r*0.32}" cy="{ey}" r="{r*0.09}" fill="#5D4037"/><path d="M{cx+r*0.18} {ey} h{r*0.28}" stroke="#5D4037" stroke-width="{lw*0.7}" stroke-linecap="round"/>'
        elif mood == "cool":
            s += f'<path d="M{cx-r*0.6} {ey-r*0.1} h{r*1.2} l-{r*0.1} {r*0.25} h-{r*0.35} l-{r*0.1} -{r*0.15} l-{r*0.1} {r*0.15} h-{r*0.35}z" fill="#212121"/>'
        else:
            s += f'<circle cx="{cx-r*0.32}" cy="{ey}" r="{r*0.09}" fill="#5D4037"/><circle cx="{cx+r*0.32}" cy="{ey}" r="{r*0.09}" fill="#5D4037"/>'
        my = cy + r * 0.3
        if mood == "sad":
            s += f'<path d="M{cx-r*0.35} {my+r*0.12} Q{cx} {my-r*0.2} {cx+r*0.35} {my+r*0.12}" fill="none" stroke="#5D4037" stroke-width="{lw*0.7}" stroke-linecap="round"/>'
        elif mood == "surprised":
            s += f'<circle cx="{cx}" cy="{my}" r="{r*0.15}" fill="#5D4037"/>'
        elif mood == "laugh":
            s += f'<path d="M{cx-r*0.42} {my-r*0.08} Q{cx} {my+r*0.55} {cx+r*0.42} {my-r*0.08}z" fill="#5D4037"/>'
        else:
            s += f'<path d="M{cx-r*0.38} {my-r*0.05} Q{cx} {my+r*0.35} {cx+r*0.38} {my-r*0.05}" fill="none" stroke="#5D4037" stroke-width="{lw*0.7}" stroke-linecap="round"/>'
        return s
    d = {
        "arrow": f'<path d="M{x0+r*0.2} {cy+r*0.6} L{x0+r*1.75} {cy-r*0.55} M{x0+r*1.75} {cy-r*0.55} l-{r*0.55} {r*0.05} M{x0+r*1.75} {cy-r*0.55} l-{r*0.15} {r*0.5}" {sl}/>',
        "block": f'<path d="M{x0+r*0.15} {cy-r*0.25} h{r*0.95} v-{r*0.4} l{r*0.75} {r*0.65} l-{r*0.75} {r*0.65} v-{r*0.4} h-{r*0.95}z" {st} {fl}/>',
        "curved": f'<path d="M{x0+r*0.25} {cy+r*0.6} Q{x0+r*0.4} {cy-r*0.7} {x0+r*1.7} {cy-r*0.4} M{x0+r*1.7} {cy-r*0.4} l-{r*0.5} -{r*0.25} M{x0+r*1.7} {cy-r*0.4} l-{r*0.35} {r*0.4}" {sl}/>',
        "rect": f'<rect x="{x0+r*0.2}" y="{cy-r*0.55}" width="{r*1.6}" height="{r*1.1}" {st} {fl}/>',
        "rounded": f'<rect x="{x0+r*0.2}" y="{cy-r*0.55}" width="{r*1.6}" height="{r*1.1}" rx="{r*0.3}" {st} {fl}/>',
        "circle": f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.8}" ry="{r*0.8}" {st} {fl}/>',
        "star": '<path d="' + "M" + " L".join(f"{cx + (r*0.85 if i % 2 == 0 else r*0.38) * __import__('math').sin(i*3.14159/5)} {cy - (r*0.85 if i % 2 == 0 else r*0.38) * __import__('math').cos(i*3.14159/5)}" for i in range(10)) + f'z" {st} {fl}/>',
        "line": f'<path d="M{x0+r*0.25} {cy+r*0.5} L{x0+r*1.75} {cy-r*0.5}" {sl}/>',
        "bubble": f'<path d="M{x0+r*0.4} {cy-r*0.6} h{r*1.2} q{r*0.25} 0 {r*0.25} {r*0.25} v{r*0.55} q0 {r*0.25} -{r*0.25} {r*0.25} h-{r*0.7} l-{r*0.4} {r*0.35} v-{r*0.35} h-{r*0.1} q-{r*0.25} 0 -{r*0.25} -{r*0.25} v-{r*0.55} q0 -{r*0.25} {r*0.25} -{r*0.25}z" {st} {fl}/>',
        "marker": f'<rect x="{x0+r*0.15}" y="{cy-r*0.25}" width="{r*1.7}" height="{r*0.5}" rx="{r*0.08}" fill="{YELLOW}" fill-opacity="0.6"/>',
        "tick": f'<path d="M{x0+r*0.3} {cy} l{r*0.45} {r*0.45} l{r*0.95} -{r*0.95}" {sl}/>'.replace(line, "#43A047"),
        "cross": f'<path d="M{x0+r*0.4} {cy-r*0.6} l{r*1.2} {r*1.2} M{x0+r*1.6} {cy-r*0.6} l-{r*1.2} {r*1.2}" {sl}/>',
    }
    return d[name]


SMILEYS = ["smiley_happy", "smiley_laugh", "smiley_wink", "smiley_sad", "smiley_surprised", "smiley_cool"]
OTHERS = ["arrow", "block", "curved", "rect", "rounded", "circle", "star", "line", "bubble", "marker", "tick", "cross"]


def graphic_picker():
    def c(top):
        s = t(16, top + 52, "Graphic", 18, TEXT, 600)
        s += t(16, top + 74, "Appears at the pointer, in the middle of the video", 13, MUTED)
        cell, gap = 46, 9
        for row, names in enumerate([SMILEYS, OTHERS[:6], OTHERS[6:]]):
            for i, n in enumerate(names):
                x = 16 + i * (cell + gap)
                y = top + 94 + row * (cell + gap)
                s += rect(x, y, cell, cell, SURF_HI, 10, OUTLINE, 1)
                s += shape_art(n, x + cell / 2, y + cell / 2, cell * 0.72, fill=RED if n in ("block", "rect", "rounded", "circle", "star", "bubble") else None)
        y = top + 94 + 3 * (cell + gap) + 6
        s += outline_button(16, y, 250, 42, "Your own picture from Gallery", "image")
        return s
    return editor() + sheet(330, c)


def graphic_editor():
    s = status_bar()
    s += icon("back", 28, 52, 24, TEXT) + t(56, 49, "Lysá hora flight", 16, TEXT, 600)
    s += t(56, 66, "1920×1080 · 50 fps · 2:31", 12, MUTED, 400, mono=True) + button(264, 32, 84, 40, "Export")
    vh = W * 9 / 16
    s += rect(0, 80, W, PANEL_TOP - 80, "#000") + landscape(0, SUB_VY, W, vh, 0, "ge")
    # a curved arrow pointing at the glider (top right of the frame)
    x0, y0, w0, h0 = W * 0.42, SUB_VY + vh * 0.32, W * 0.24, vh * 0.34
    s += shape_art("curved", x0 + w0 / 2, y0 + h0 / 2, min(w0, h0) * 1.25, "#FF7043", lw=4)
    s += f'<rect x="{x0}" y="{y0}" width="{w0}" height="{h0}" fill="none" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="5 4"/>'
    for cx, cy in ((x0, y0), (x0 + w0, y0), (x0, y0 + h0), (x0 + w0, y0 + h0)):
        s += f'<circle cx="{cx}" cy="{cy}" r="8.5" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="7" fill="{ACCENT}"/>'
    s += rotate_handle(x0 + w0 / 2, y0)
    top = PANEL_TOP
    s += rect(0, top, W, H - top, SURF)
    s += t(16, top + 30, "Curved arrow", 16, TEXT, 600)
    s += icon("play", 238, top + 24, 24, TEXT) + icon("trash", 280, top + 24, 22, DEL_LINE)
    s += button(300, top + 6, 52, 36, "Done")
    tw = (W - 16) / 3
    for i, lab in enumerate(["Shape", "Look", "Motion"]):
        sel = lab == "Look"
        s += t(8 + tw * i + tw / 2, top + 68, lab, 14, ACCENT if sel else MUTED, 600 if sel else 400, "middle")
        s += rect(8 + tw * i, top + 80, tw, 2, ACCENT if sel else OUTLINE)
    y = top + 106
    s += t(16, y, "Line", 14)
    sw = ["#FFFFFF", "#000000", "#FFEB3B", "#FF7043", "#E53935", "#43A047", "#00BCD4", "#1E88E5", "#D81B60"]
    for i, c in enumerate(sw):
        cx = 32 + i * 42
        sel = c == "#FF7043"
        s += f'<circle cx="{cx}" cy="{y + 30}" r="16" fill="none" stroke="{ACCENT if sel else OUTLINE}" stroke-width="{3 if sel else 1}"/>'
        s += f'<circle cx="{cx}" cy="{y + 30}" r="{11 if sel else 13}" fill="{c}"/>'
    s += slider(y + 72, "Width", "1.2 %", 0.3)
    s += slider(y + 120, "Opacity", "100 %", 1.0)
    s += t(16, y + 168, "Position (or drag it on the video)", 13, MUTED)
    s += chips(16, y + 178, ["Top", "Middle", "Bottom", "Centre"])
    s += t(16, y + 240, "Rotation", 14) + t(16, y + 256, "Turn it with the round handle on the video", 12, MUTED)
    s += t(W - 76, y + 246, "0°", 14, TEXT, 400, "end", True) + t(W - 24, y + 246, "Reset", 14, MUTED, 500, "end")
    return s + nav_bar()


# ---------------------------------------------------------------- path capture (ui/PathCapture.kt)
def path_capture():
    s = status_bar()
    top = 24
    s += rect(0, top, W, 132, SURF)
    s += t(18, top + 30, "Cancel", 14, ACCENT, 600) + t(W / 2, top + 30, "Capture path", 16, TEXT, 600, "middle")
    s += button(W - 76, top + 10, 64, 36, "Done")
    for i, line in enumerate(["Hold your finger on the anchor. After a moment the",
                              "video plays while you move, so you can follow",
                              "what you want to track."]):
        s += t(W / 2, top + 64 + i * 17, line, 12.5, MUTED, 400, "middle")
    by, bw = top + 112, W - 24
    s += rect(12, by, bw, 8, BG, 4) + rect(12 + bw * 0.12, by, bw * 0.78, 8, "#ffffff", op=0.22)
    s += rect(12, by, bw * 0.12, 8, ACCENT, 0, op=0.35) + rect(12 + bw * 0.12, by, bw * 0.39, 8, ACCENT)
    s += rect(12, by, bw, 8, "none", 4, OUTLINE, 1)
    # preview: frame outlined, outside dimmed
    ptop, pbot = top + 132, H - 24 - 96
    s += rect(0, ptop, W, pbot - ptop, "#000")
    vh = W * 9 / 16
    vy = ptop + (pbot - ptop - vh) / 2
    s += landscape(0, vy, W, vh, 0, "pc")
    s += rect(0, ptop, W, vy - ptop, "#000", op=0.6) + rect(0, vy + vh, W, pbot - vy - vh, "#000", op=0.6)
    s += f'<rect x="1" y="{vy}" width="{W-2}" height="{vh}" fill="none" stroke="#fff" stroke-opacity="0.7" stroke-width="1.5"/>'
    # recorded track so far, and the arrow riding on it next to the glider
    gx, gy = 228 * W / 320, vy + 58 * vh / 180
    s += (f'<path d="M{W*0.12} {vy+vh*0.62} C{W*0.3} {vy+vh*0.5}, {W*0.5} {vy+vh*0.45}, {gx-34} {gy+30}" fill="none" '
          f'stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" stroke-opacity="0.85"/>')
    ax, ay = gx - 34, gy + 30
    s += shape_art("curved", ax, ay, 44, "#FF7043", lw=3.5)
    s += f'<circle cx="{ax}" cy="{ay}" r="13" fill="none" stroke="#fff" stroke-width="2.5"/><circle cx="{ax}" cy="{ay}" r="3" fill="#fff"/>'
    s += f'<circle cx="{ax+10}" cy="{ay+26}" r="22" fill="#fff" fill-opacity="0.18" stroke="#fff" stroke-opacity="0.5"/>'
    # bottom bar
    s += rect(0, pbot, W, 96, SURF)
    s += t(12, pbot + 24, "Recording… 2.5 s of 5.0 s · lift your finger", 13, ACCENT)
    s += t(12, pbot + 41, "to finish", 13, ACCENT)
    s += chips(12, pbot + 52, ["Steps", "Smooth"], ("Smooth",))
    s += chips(176, pbot + 52, ["½×", "1×"], ("1×",))
    return s + nav_bar()


# ---------------------------------------------------------------- text slide (ui/SlideDialog.kt)
def slide_art(x, y, w, h, title, line2, uid, scale=1.0, template="gradient"):
    s = f'<defs><linearGradient id="sl{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1E3A5F"/><stop offset="1" stop-color="#E5532F"/></linearGradient></defs>'
    if template == "gradient":
        s += rect(x, y, w, h, f"url(#sl{uid})", 4 * scale)
    elif template == "band":
        s += rect(x, y, w, h, "#10151C", 4 * scale) + rect(x, y + h * 0.36, w, h * 0.3, "#E5532F")
    elif template == "cinema":
        s += rect(x, y, w, h, "#000", 4 * scale) + rect(x, y + h * 0.15, w, h * 0.7, "#1E3A5F")
    elif template == "frame":
        s += rect(x, y, w, h, "#1E3A5F", 4 * scale) + rect(x + w * 0.06, y + h * 0.1, w * 0.88, h * 0.8, "none", 0, "#F2F2F0", 1.2 * scale)
    elif template == "split":
        s += rect(x, y, w, h, "#1E3A5F", 4 * scale) + rect(x + w / 2, y, w / 2, h, "#E5532F")
    elif template == "minimal":
        s += rect(x, y, w, h, "#F2F2F0", 4 * scale)
    else:  # classic
        s += rect(x, y, w, h, "#1E3A5F", 4 * scale)
    col = "#10151C" if template == "minimal" else "#FFFFFF"
    s += t(x + w / 2, y + h * 0.5, title, h * 0.16, col, 700, "middle")
    if line2:
        s += t(x + w / 2, y + h * 0.68, line2, h * 0.08, col, 400, "middle")
    return s


def text_slide_sheet():
    def c(top):
        s = t(16, top + 50, "Text slide", 18, TEXT, 600) + button(W - 104, top + 28, 88, 40, "Insert")
        pw = W - 32
        s += slide_art(16, top + 82, pw, pw * 9 / 16, "Lysá hora", "First flight of the season", "big")
        y = top + 82 + pw * 9 / 16 + 14
        s += rect(16, y, W - 32, 52, "none", 4, MUTED, 1) + t(26, y - 2, "Title", 11, MUTED).replace('y="', 'y="', 1)
        s += rect(24, y - 8, 34, 12, SURF) + t(28, y + 2, "Title", 11, MUTED) + t(30, y + 32, "Lysá hora", 15)
        y += 64
        s += rect(16, y, W - 32, 52, "none", 4, MUTED, 1) + rect(24, y - 8, 152, 12, SURF) + t(28, y + 2, "Second line (optional)", 11, MUTED)
        s += t(30, y + 32, "First flight of the season", 15)
        y += 66
        tw = (W - 32) / 2
        for i, lab in enumerate(["Templates", "Customize"]):
            sel = i == 0
            s += t(16 + tw * i + tw / 2, y + 14, lab, 14, ACCENT if sel else MUTED, 600 if sel else 400, "middle")
            s += rect(16 + tw * i, y + 24, tw, 2, ACCENT if sel else OUTLINE)
        y += 38
        tiles = [("Classic", "classic"), ("Gradient", "gradient"), ("Band", "band"), ("Cinema", "cinema"), ("Minimal", "minimal")]
        for i, (lab, tpl) in enumerate(tiles):
            x = 16 + i * 84
            sel = tpl == "gradient"
            s += slide_art(x, y, 76, 43, "Lysá hora", "", f"t{i}", 0.5, tpl)
            if sel:
                s += rect(x - 2, y - 2, 80, 47, "none", 6, ACCENT, 2)
            s += t(x + 38, y + 60, lab, 12, ACCENT if sel else MUTED, 400, "middle")
        y += 84
        s += t(16, y + 22, "Shown for", 14) + stepper(W - 16 - 136, y, "4.0 s")
        return s
    return editor() + sheet(H - 40, c)


# ---------------------------------------------------------------- transitions at every join (ui/Sheets.kt)
def switch(x, y, on):
    s = rect(x, y, 52, 32, ACCENT if on else SURF, 16, None if on else MUTED, 2)
    return s + f'<circle cx="{x + (36 if on else 16)}" cy="{y + 16}" r="{12 if on else 8}" fill="{ON_ACCENT if on else MUTED}"/>'


def every_join_dialog():
    def body(x, y, w):
        s = t(x, y + 6, "Type", 13, MUTED)
        s += radio(x + 10, y + 32, True) + t(x + 30, y + 30, "Fade out-in", 15) + t(x + 30, y + 46, "Dips to black and back", 12, MUTED)
        s += radio(x + 10, y + 80, False) + t(x + 30, y + 78, "Interleave", 15) + rect(x + 112, y + 66, 34, 15, ACCENT, 7) + t(x + 129, y + 77, "PRO", 9, ON_ACCENT, 900, "middle") + t(x + 30, y + 94, "Crossfade. The video gets shorter", 12, MUTED)
        s += t(x, y + 136, "Duration", 14) + t(x, y + 153, "Each, in the", 12, MUTED) + t(x, y + 168, "export", 12, MUTED)
        s += stepper(x + w - 136, y + 122, "2.0 s")
        s += t(x, y + 208, "Fade in & out", 15) + t(x, y + 225, "At the start and the end", 12, MUTED) + t(x, y + 240, "of the video", 12, MUTED)
        s += switch(x + w - 52, y + 200, True)
        s += t(x, y + 280, "Replace existing", 15) + t(x, y + 297, "Otherwise only joins without", 12, MUTED) + t(x, y + 312, "one get it", 12, MUTED)
        s += switch(x + w - 52, y + 272, False)
        s += t(x, y + 346, "Adds 3 transitions.", 12, ACCENT)
        return s
    return editor(transition_set=(1,)) + dialog(500, "Transitions at every join", body, [("Cancel", ACCENT), ("Apply", ACCENT)], width=330)


# ---------------------------------------------------------------- tablet, landscape (EditorScreen wide layout)
TW, TH = 960, 600            # a 7–8" tablet held sideways, in dp
T_BOTTOM = TH - 24 - 76      # top of the bottom row: transport on the left, tools on the right
T_TL_TOP = T_BOTTOM - 196    # timeline block (labels, strip, subtitles, zoom row)
T_TOOLS_W = 480              # WIDE_TOOLBAR_WIDTH
T_PANEL_W = 400              # OVERLAY_PANEL_WIDTH


def t_frame(body):
    bar = (rect(0, 0, TW, 24, BG) + t(16, 17, "10:18", 12, TEXT, 500)
           + rect(TW - 44, 9, 22, 10, "none", 2, TEXT, 1.2) + rect(TW - 42, 11, 14, 6, TEXT, 1))
    nav = rect(0, TH - 24, TW, 24, BG) + rect(TW / 2 - 54, TH - 14, 108, 4, MUTED, 2)
    return bar + body + nav


def t_header():
    title = "Lysá hora flight"
    return (icon("back", 28, 52, 24, TEXT) + t(56, 49, title, 16, TEXT, 600)
            + icon("edit", 56 + len(title) * 9.2 + 10, 44, 14, MUTED)
            + t(56, 66, "1920×1080 · 50 fps · 2:31", 12, MUTED, 400, mono=True)
            + button(TW - 96, 32, 84, 40, "Export"))


def t_preview(x, y, w, h, subtitle="", box=False):
    s = rect(x, y, w, h, "#000")
    vw = min(w, h * 16 / 9)
    vh = vw * 9 / 16
    vx, vy = x + (w - vw) / 2, y + (h - vh) / 2
    s += landscape(vx, vy, vw, vh, 0, f"tp{int(w)}")
    if subtitle:
        bx, by, bw, bh = SUB_BOX
        x0, y0, w0, h0 = vx + bx * vw, vy + by * vh, bw * vw, bh * vh
        s += rect(x0, y0, w0, h0, "#000", 4, op=0.72) + t(vx + vw / 2, y0 + h0 / 2 + 5, subtitle, 15, "#fff", 400, "middle")
        if box:
            s += f'<rect x="{x0}" y="{y0}" width="{w0}" height="{h0}" fill="none" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="5 4"/>'
            for cx, cy in ((x0, y0), (x0 + w0, y0), (x0, y0 + h0), (x0 + w0, y0 + h0)):
                s += f'<circle cx="{cx}" cy="{cy}" r="8.5" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="7" fill="{ACCENT}"/>'
    else:
        s += rect(vx + 10, vy + 10, 36, 20, "#000", 4, op=0.6) + t(vx + 28, vy + 24, "4×", 12, ACCENT, 600, "middle", True)
    return s


def t_timeline(top):
    tl_x, tl_w = 16, TW - 20
    s = ""
    for i, lab in enumerate(["0:00", "0:37", "1:15", "1:53", "2:31"]):
        anchor = "start" if i == 0 else ("end" if i == 4 else "middle")
        s += t(tl_x + tl_w * i / 4, top + 18, lab, 11, MUTED, 400, anchor, True)
    tt, th = top + 36, 84
    x = tl_x
    bounds = []
    for i, (frac, lab, fast, _d, sel) in enumerate(DEFAULT_SEGS):
        w = tl_w * frac
        left, right = x + (1 if i else 0), x + w - (1 if i < 2 else 0)
        s += f'<clipPath id="tsg{i}"><rect x="{left}" y="{tt}" width="{right-left}" height="{th}" rx="6"/></clipPath><g clip-path="url(#tsg{i})">'
        s += rect(left, tt, right - left, th, SEG) + tile_band(left, tt, right - left, th, False, f"ttb{i}") + "</g>"
        if sel:
            s += rect(left, tt, right - left, th, "none", 6, ACCENT, 2.5)
            s += f'<circle cx="{right-20}" cy="{tt+20}" r="12" fill="#000" fill-opacity="0.6"/>' + icon("info", right - 20, tt + 20, 18, TEXT)
        lw = len(lab) * 7.2 + 6
        s += rect(left + 3, tt + th - 24, lw, 18, "#000", 3, op=0.55)
        s += t(left + 6, tt + th - 11, lab, 12, ACCENT if (sel or fast) else TEXT, 500, mono=True)
        if i:
            bounds.append(x)
        x += w
    for bx in bounds:
        s += f'<line x1="{bx}" y1="{tt-2}" x2="{bx}" y2="{tt+th}" stroke="{ACCENT}" stroke-width="2"/>'
        s += f'<path d="M{bx-6} {tt-12} H{bx+6} L{bx} {tt-1}Z" fill="{ACCENT}"/>'
    for jx in [tl_x] + bounds + [tl_x + tl_w]:
        cxp = min(max(jx, tl_x + 18), tl_x + tl_w - 18)
        s += f'<circle cx="{cxp}" cy="{tt+th/2}" r="13" fill="#000" fill-opacity="0.65"/>' + icon("fade", cxp, tt + th / 2, 16, TEXT)
    px = tl_x + tl_w * 0.47
    s += f'<line x1="{px}" y1="{tt-4}" x2="{px}" y2="{tt+th}" stroke="#fff" stroke-width="2"/><circle cx="{px}" cy="{tt-4}" r="5" fill="#fff"/>'
    sy = tt + th + 6
    for a, b, txt in ((0.08, 0.30, "Take-off from Lysá hora"), (0.70, 0.93, "Landing")):
        s += rect(tl_x + tl_w * a, sy, tl_w * (b - a), 28, SUB, 5)
        s += icon("title", tl_x + tl_w * a + 9, sy + 14, 12, SUB_TEXT + "BF") + t(tl_x + tl_w * a + 18, sy + 18, txt, 11, SUB_TEXT)
    zy = sy + 28 + 22
    s += icon("eye_off", 40, zy, 22, MUTED) + icon("zoom_out", 86, zy, 22, MUTED + "66")
    s += rect(112, zy - 2, TW - 112 - 60, 4, SURF, 2) + f'<circle cx="120" cy="{zy}" r="8" fill="{MUTED}" fill-opacity="0.4"/>'
    s += icon("zoom_in", TW - 28, zy, 22, TEXT)
    return s


def t_bottom_row():
    cy = T_BOTTOM + 38
    s = icon("skip_prev", 28, cy, 22, TEXT) + icon("replay5", 68, cy, 22, TEXT)
    s += f'<circle cx="110" cy="{cy}" r="22" fill="{SURF_HI}"/>' + icon("play", 110, cy, 24, TEXT)
    s += icon("forward5", 152, cy, 22, TEXT) + icon("skip_next", 192, cy, 22, TEXT)
    s += t(216, cy - 3, "0:21.4", 11, TEXT, 400, mono=True) + t(216, cy + 11, "0:48.0", 11, MUTED, 400, mono=True)
    s += icon("undo", TW - T_TOOLS_W - 28, cy, 24, TEXT)
    bw = (T_TOOLS_W - 8) / 7
    for i, (ic, lab) in enumerate([("cut", "Split"), ("trash", "Delete"), ("speed", "Speed"),
                                   ("volume", "Mute"), ("subs", "Text"), ("category", "Graphic"), ("plus", "Add")]):
        bx = TW - T_TOOLS_W + 4 + bw * i + bw / 2
        s += icon(ic, bx, cy - 10, 22, TEXT) + t(bx, cy + 18, lab, 12, TEXT, 400, "middle")
    return s


def tablet_editor():
    return t_frame(t_header() + t_preview(0, 80, TW, T_TL_TOP - 80) + t_timeline(T_TL_TOP) + t_bottom_row())


def tablet_subtitle():
    top, px = 80, TW - T_PANEL_W
    s = t_header() + t_preview(0, top, px, TH - 24 - top, "Take-off from Lysá hora", box=True)
    s += rect(px, top, T_PANEL_W, TH - 24 - top, SURF)
    s += t(px + 16, top + 30, "Text", 16, TEXT, 600)
    s += icon("play", TW - 122, top + 24, 24, TEXT) + icon("trash", TW - 80, top + 24, 22, DEL_LINE)
    s += button(TW - 60, top + 6, 52, 36, "Done")
    tw = (T_PANEL_W - 16) / 3
    for i, lab in enumerate(["Text", "Look", "Motion"]):
        sel = i == 0
        s += t(px + 8 + tw * i + tw / 2, top + 68, lab, 14, ACCENT if sel else MUTED, 600 if sel else 400, "middle")
        s += rect(px + 8 + tw * i, top + 80, tw, 2, ACCENT if sel else OUTLINE)
    y = top + 98
    s += rect(px + 16, y, T_PANEL_W - 32, 56, "none", 4, MUTED, 1) + t(px + 32, y + 33, "Take-off from Lysá hora", 16)
    s += t(px + 16, y + 86, "Duration", 14) + t(px + 16, y + 103, "On screen in the export", 12, MUTED)
    s += stepper(TW - 16 - 136, y + 72, "5.0 s")
    s += t(px + 16, y + 144, "Starts at", 14)
    bxs = px + 16
    for lab in ["−1 s", "−0.1"]:
        w = len(lab) * 7.5 + 18
        s += rect(bxs, y + 154, w, 38, "none", 19, OUTLINE, 1) + t(bxs + w / 2, y + 178, lab, 13, ACCENT, 600, "middle")
        bxs += w + 6
    s += t(px + T_PANEL_W / 2, y + 178, "0:12.0", 16, TEXT, 400, "middle", True)
    bxe = TW - 16
    for lab in ["+1 s", "+0.1"]:
        w = len(lab) * 7.5 + 18
        bxe -= w
        s += rect(bxe, y + 154, w, 38, "none", 19, OUTLINE, 1) + t(bxe + w / 2, y + 178, lab, 13, ACCENT, 600, "middle")
        bxe -= 6
    s += t(px + 16, y + 212, "Or drag the text along the timeline", 12, MUTED)
    return t_frame(s)


TABLET_SCREENS = {
    "tablet-editor": lambda: tablet_editor()
        + callout(1, 30, 100, ring=(8, 84, TW - 16, T_TL_TOP - 88))
        + callout(2, 140, T_TL_TOP + 6, ring=(8, T_TL_TOP + 4, TW - 16, 192))
        + callout(3, 30, T_BOTTOM + 8, ring=(8, T_BOTTOM + 12, TW - T_TOOLS_W - 4, 52))
        + callout(4, TW - T_TOOLS_W + 10, T_BOTTOM + 8, ring=(TW - T_TOOLS_W + 2, T_BOTTOM + 6, T_TOOLS_W - 8, 64)),
    "tablet-subtitle": lambda: tablet_subtitle()
        + callout(1, 30, 100, ring=(8, 84, TW - T_PANEL_W - 16, TH - 24 - 92))
        + callout(2, TW - T_PANEL_W + 20, TH - 44, ring=(TW - T_PANEL_W + 4, 84, T_PANEL_W - 8, TH - 24 - 92)),
}


SCREENS = {
    "home-empty": lambda: home(projects=False),
    "home": lambda: home() + callout(1, 196, 98, ring=(178, 38, 38, 40)) + callout(2, 284, 94, ring=(220, 34, 128, 48))
            + callout(3, 50, 206, ring=(10, 128, 340, 76)) + callout(4, 334, 176, ring=(316, 146, 36, 36)),
    "new-project": lambda: home(sheet=True),
    "project-menu": lambda: home(menu=True),
    "rename-project": rename_dialog,
    "delete-project": delete_project_dialog,
    "editor": lambda: editor()
              + callout(1, 150, 92, ring=(48, 32, 200, 40)) + callout(2, 306, 92, ring=(262, 30, 88, 44))
              + callout(3, 300, 136) + callout(4, 12, 434, ring=(8, 432, 266, 52)) + callout(5, 312, 434, ring=(310, 432, 48, 48))
              + callout(6, 14, TL_TRACK_TOP + 40, ring=(12, TL_TRACK_TOP - 16, 348, 102))
              + callout(7, 14, TL_TRACK_TOP + 104, ring=(12, TL_TRACK_TOP + 89, 348, 30))
              + callout(8, 14, TL_TRACK_TOP + 144, ring=(12, TL_TRACK_TOP + 125, 348, 38))
              + callout(9, 14, TOOL_Y + 37, ring=(10, TOOL_Y + 6, 344, 62)),
    "split": lambda: editor(segs=SPLIT_SEGS, playhead=0.47, subs=(), speed_badge="", time="1:11.0", total="2:31.0", transitions=False)
             + callout(1, 16 + 340 * 0.47 + 18, TL_TRACK_TOP - 14, ring=(16 + 340 * 0.47 - 12, TL_TRACK_TOP - 14, 24, 100))
             + callout(2, TOOL_X[0] + 26, TOOL_Y + 4, ring=tool_ring(0)),
    "delete": lambda: editor(segs=DEL_SEGS, selected_deleted=True, show_deleted=True, speed_badge="", total="0:38.7", transitions=False)
              + callout(1, 16 + 340 * 0.51, TL_TRACK_TOP - 16, ring=(16 + 340 * 0.36, TL_TRACK_TOP, 340 * 0.30, 84))
              + callout(2, TOOL_X[1] + 26, TOOL_Y + 4, ring=tool_ring(1))
              + callout(3, 60, TL_TRACK_TOP + 150, ring=(20, TL_TRACK_TOP + 128, 40, 40)),
    "speed": speed_sheet,
    "subtitle-editor": lambda: subtitle_editor("Text")
                       + callout(1, SUB_BOX_PX[0] + 60, SUB_BOX_PX[1] - 16)
                       + callout(7, SUB_BOX_PX[0] + SUB_BOX_PX[2] / 2 + 30, SUB_BOX_PX[1] - 32)
                       + callout(2, SUB_BOX_PX[0] + SUB_BOX_PX[2] + 2, SUB_BOX_PX[1] + SUB_BOX_PX[3] + 18)
                       + callout(3, 16 + 4, PANEL_TOP + 52, ring=(8, PANEL_TOP + 50, W - 16, 36))
                       + callout(4, W - 12, PANEL_TOP + 98 + 176, ring=(10, PANEL_TOP + 98 + 128, W - 20, 70))
                       + callout(5, 226, PANEL_TOP + 8, ring=(222, PANEL_TOP + 6, 34, 36))
                       + callout(6, 342, PANEL_TOP + 52, ring=(298, PANEL_TOP + 4, 56, 40)),
    "subtitle-look": lambda: subtitle_editor("Look", look="styled"),
    "subtitle-motion": lambda: subtitle_editor("Motion", look="styled"),
    "subtitles-timeline": lambda: editor(subtitle_on_preview="Take-off from Lysá hora", speed_badge="", playhead=0.2)
                          + callout(1, 16 + 340 * 0.19, TL_TRACK_TOP + 106, ring=(16 + 340 * 0.08 - 4, TL_TRACK_TOP + 86, 340 * 0.22 + 8, 36))
                          + callout(2, TOOL_X[4] + 26, TOOL_Y + 4, ring=tool_ring(4)),
    "transition-buttons": lambda: editor(transition_set=(1,))
                          + callout(1, 16 + 340 * 0.36, TL_TRACK_TOP + 14, ring=(16 + 340 * 0.36 - 18, TL_TRACK_TOP + 24, 36, 36))
                          + callout(2, 34, TL_TRACK_TOP + 14, ring=(16, TL_TRACK_TOP + 24, 36, 36)),
    "transition": transition_dialog,
    "segment-info": segment_info,
    "export": export_sheet,
    "export-progress": export_running,
    "export-done": export_done,
    "missing-video": missing_video,
    "add": add_sheet,
    "media-timeline": lambda: editor(segs=MEDIA_SEGS, speed_badge="", preview_shade=1, selected_picture=True, playhead=0.33,
                                     soundtracks=((0.08, 0.62, "Sunrise over the ridge", False), (0.62, 1.0, "Wind", True)),
                                     title="Ramzová day", time="0:15.1", total="0:52.0")
                      + callout(1, 16 + 340 * 0.40, MEDIA_TOP - 14, ring=(16 + 340 * 0.26, MEDIA_TOP, 340 * 0.18, 84))
                      + callout(2, 16 + 340 * 0.72, MEDIA_TOP - 14, ring=(16 + 340 * 0.72 - 8, MEDIA_TOP, 16, 84))
                      + callout(3, 16 + 340 * 0.44 + 92, MEDIA_TOP + 69, ring=(16 + 340 * 0.44 + 2, MEDIA_TOP + 58, 82, 22))
                      + callout(4, 30, MEDIA_TOP + 132, ring=(18, MEDIA_TOP + 120, 344, 26))
                      + callout(5, TOOL_X[6] - 22, TOOL_Y + 4, ring=tool_ring(6)),
    "mute": lambda: editor(segs=[(0.36, "1×", False, False, False), (0.30, "1× · muted", False, False, True), (0.34, "1×", False, False, False)],
                           speed_badge="", selected_muted=True, transitions=False)
                    + callout(1, 16 + 340 * 0.51, TL_TRACK_TOP - 16, ring=(16 + 340 * 0.36, TL_TRACK_TOP, 340 * 0.30, 84))
                    + callout(2, TOOL_X[3] + 26, TOOL_Y + 4, ring=tool_ring(3)),
    "picture-add": picture_dialog,
    "soundtrack": soundtrack_dialog,
    "segment-info-picture": segment_info_picture,
    "welcome": lambda: welcome() + callout(1, W / 2 - 134, 438, ring=(W / 2 - 122, 424, 244, 28)) + callout(2, W / 2 + 72, 520, ring=(W / 2 - 60, 496, 120, 48))
               + callout(3, 30, 676, ring=(16, 686, 106, 56)) + callout(4, W - 30, 676, ring=(124, 686, W - 140, 56)),
    "settings-edition": lambda: settings_sheet() + callout(1, 182, 575, ring=(26, 572, 144, 48)),
    "graphic-picker": graphic_picker,
    "graphic-editor": graphic_editor,
    "path-capture": path_capture,
    "path-row": lambda: subtitle_editor("Path", look="classic"),
    "text-slide": text_slide_sheet,
    "transitions-every-join": every_join_dialog,
}


def main(names=None):
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SCREENS.items():
        if names and name not in names:
            continue
        svg = phone(fn())
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, f"{name}.png"), output_width=W * 2, output_height=H * 2)
        print("wrote", name)
    for name, fn in TABLET_SCREENS.items():
        if names and name not in names:
            continue
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW}" height="{TH}" viewBox="0 0 {TW} {TH}">'
               + rect(0, 0, TW, TH, BG) + fn() + "</svg>")
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, f"{name}.png"), output_width=TW * 2, output_height=TH * 2)
        print("wrote", name)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
