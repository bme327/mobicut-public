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
CALLOUT = "#3FA9F5"

W, H = 360, 780
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
        rows = [("Lysá hora flight", "3 segments · 2 subtitles", "Edited 5 minutes ago", "0:48", 0),
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
           video=True):
    s = status_bar()
    # header
    s += icon("back", 28, 52, 24, TEXT)
    s += t(56, 49, title, 16, TEXT, 600)
    s += icon("edit", 56 + len(title) * 8.6 + 10, 44, 14, MUTED)
    s += t(56, 66, "1920×1080 · 50 fps · 2:31", 12, MUTED, 400, mono=True)
    s += button(264, 32, 84, 40, "Export")
    # preview
    pv_top, pv_h = 80, 346
    s += rect(0, pv_top, W, pv_h, "#000")
    if video:
        vh = W * 9 / 16
        vy = pv_top + (pv_h - vh) / 2
        s += landscape(0, vy, W, vh, 0, "pv")
        if speed_badge:
            s += rect(10, vy + 10, 36, 20, "#000", 4, op=0.6) + t(28, vy + 24, speed_badge, 12, ACCENT, 600, "middle", True)
        if subtitle_on_preview:
            tw = len(subtitle_on_preview) * 7.6 + 20
            s += rect(W / 2 - tw / 2, vy + vh - 40, tw, 26, "#000", 4, op=0.72)
            s += t(W / 2, vy + vh - 22, subtitle_on_preview, 15, "#fff", 400, "middle")
    # controls
    cy = pv_top + pv_h
    s += f'<circle cx="38" cy="{cy+30}" r="22" fill="{SURF_HI}"/>' + icon("pause" if playing else "play", 38, cy + 30, 24, TEXT)
    s += t(72, cy + 35, time, 14, TEXT, 400, mono=True) + t(132, cy + 35, "/ " + total, 14, MUTED, 400, mono=True)
    s += icon("undo", 330, cy + 30, 24, TEXT)
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
    for i, (frac, lab, fast, deleted, sel) in enumerate(segs):
        w = tl_w * frac
        left = x + (1 if i > 0 else 0)
        right = x + w - (1 if i < len(segs) - 1 else 0)
        s += f'<clipPath id="sg{i}"><rect x="{left}" y="{track_top}" width="{right-left}" height="{track_h}" rx="6"/></clipPath><g clip-path="url(#sg{i})">'
        s += rect(left, track_top, right - left, track_h, SEG)
        if video:
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
            bounds.append(x)
        x += w
    for bx in bounds:
        s += f'<line x1="{bx}" y1="{track_top-2}" x2="{bx}" y2="{track_top+track_h}" stroke="{ACCENT}" stroke-width="2"/>'
        s += f'<path d="M{bx-6} {track_top-12} H{bx+6} L{bx} {track_top-1}Z" fill="{ACCENT}"/>'
    if transitions and not show_deleted:
        joins = [tl_x] + bounds + [tl_x + tl_w]
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
        s += t(tl_x, sy + 18, "Subtitles appear here", 11, MUTED, extra='fill-opacity="0.6"')
    for a, b, txt in subs:
        s += f'<clipPath id="st{a}"><rect x="{tl_x+tl_w*a}" y="{sy}" width="{tl_w*(b-a)}" height="28" rx="5"/></clipPath>'
        s += rect(tl_x + tl_w * a, sy, tl_w * (b - a), 28, SUB, 5)
        s += f'<g clip-path="url(#st{a})">' + t(tl_x + tl_w * a + 6, sy + 18, txt, 11, SUB_TEXT) + "</g>"
    # zoom row
    zy = sy + 28 + 26
    s += icon("eye" if show_deleted else "eye_off", 40, zy, 22, DEL_TEXT if show_deleted else MUTED)
    s += icon("zoom_out", 86, zy, 22, MUTED + "66")
    s += rect(112, zy - 2, 196, 4, SURF, 2) + f'<circle cx="120" cy="{zy}" r="8" fill="{MUTED}" fill-opacity="0.4"/>'
    s += icon("zoom_in", 332, zy, 22, TEXT)
    # toolbar
    ty = H - 24 - 76
    tools = [("cut", "Split"), ("restore" if selected_deleted else "trash", "Restore" if selected_deleted else "Delete"),
             ("speed", "Speed"), ("subs", "Subtitle")]
    for i, (ic, lab) in enumerate(tools):
        bx = 8 + i * 86 + 41
        s += icon(ic, bx, ty + 28, 22, TEXT) + t(bx, ty + 56, lab, 12, TEXT, 400, "middle")
    s += nav_bar()
    return s


TOOL_X = [49, 135, 221, 307]
TOOL_Y = H - 24 - 76


def tool_ring(i):
    return (TOOL_X[i] - 38, TOOL_Y + 6, 76, 62)


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
                                 ("Subtitles", ["Burn into video", "Separate .srt file", "Off"], 0)]:
            s += t(16, y, title, 13, MUTED)
            y += 8
            for i, o in enumerate(opts):
                s += radio(28, y + 22, i == sel) + t(48, y + 27, o, 15)
                y += 42
            y += 14
        s += t(16, y - 4, "If this phone can't encode the original settings,", 12, MUTED) + t(16, y + 12, "export steps down automatically.", 12, MUTED)
        s += button(16, y + 20, W - 32, 52, "Export to gallery", size=15)
        return s
    return editor() + sheet(640, c)


def export_done():
    def body(x, y, w):
        return t(x, y + 10, "Movies/MobiCut", 14, MUTED) + t(x, y + 32, "Subtitles: Download/MobiCut", 14, MUTED)
    return editor() + dialog(190, "Saved to gallery", body, [("Share", ACCENT), ("Close", ACCENT), ("Play", ACCENT)])


def export_running():
    def body(x, y, w):
        return rect(x, y + 4, w, 4, SURF, 2) + rect(x, y + 4, w * 0.42, 4, ACCENT, 2) + t(x, y + 34, "42 %  ·  keep MobiCut open", 13, MUTED)
    return editor() + dialog(180, "Exporting…", body, [("Cancel", ACCENT)])


def subtitle_dialog(edit=False):
    def body(x, y, w):
        s = rect(x, y, w, 56, "none", 4, MUTED, 1) + t(x + 16, y + 33, "Take-off from Lysá hora", 16)
        s += t(x, y + 90, "Duration", 14) + t(x, y + 107, "On screen in", 12, MUTED) + t(x, y + 122, "the export", 12, MUTED)
        s += stepper(x + w - 136, y + 76, "5.0 s")
        s += t(x, y + 150, "Starts at 0:12.0", 13, MUTED, 400, mono=True)
        if edit:
            s += rect(x, y + 166, w, 40, "none", 20, OUTLINE, 1) + t(x + w / 2, y + 191, "Start at playhead (0:21.4)", 13, ACCENT, 600, "middle")
            s += t(x + 12, y + 238, "Delete subtitle", 14, DEL_LINE, 600)
        return s
    ed = editor(subtitle_on_preview="Take-off from Lysá hora", speed_badge="")
    return ed + dialog(400 if edit else 310, "Edit subtitle" if edit else "Add subtitle", body,
                       [("Cancel", ACCENT), ("Save", ACCENT)])


def transition_dialog():
    def body(x, y, w):
        s = t(x, y + 6, "Type", 13, MUTED)
        s += radio(x + 10, y + 32, True) + t(x + 30, y + 30, "Fade out-in", 15) + t(x + 30, y + 46, "Dips to black and back", 12, MUTED)
        s += radio(x + 10, y + 80, False) + t(x + 30, y + 78, "Interleave", 15) + rect(x + 112, y + 66, 34, 15, ACCENT, 7) + t(x + 129, y + 77, "PRO", 9, ON_ACCENT, 900, "middle") + t(x + 30, y + 94, "Crossfade. The video gets shorter", 12, MUTED) + t(x + 30, y + 109, "by the duration", 12, MUTED)
        s += t(x, y + 148, "Duration", 14) + t(x, y + 165, "Total, in", 12, MUTED) + t(x, y + 180, "the export", 12, MUTED)
        s += stepper(x + w - 136, y + 134, "1.0 s")
        return s
    return editor(transition_set=(1,)) + dialog(350, "Add transition", body, [("Cancel", ACCENT), ("Save", ACCENT)])


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


# ---------------------------------------------------------------- screens with callouts
SPLIT_SEGS = [(0.47, "1×", False, False, False), (0.53, "1×", False, False, True)]
DEL_SEGS = [(0.36, "1×", False, False, False), (0.30, "4×", True, True, True), (0.34, "1×", False, False, False)]
TL_TRACK_TOP = 80 + 346 + 60 + 12 + 16

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
              + callout(3, 300, 136) + callout(4, 38, 470, ring=(12, 430, 52, 52)) + callout(5, 330, 470, ring=(306, 432, 48, 48))
              + callout(6, 14, TL_TRACK_TOP + 40, ring=(12, TL_TRACK_TOP - 16, 348, 102))
              + callout(7, 14, TL_TRACK_TOP + 104, ring=(12, TL_TRACK_TOP + 89, 348, 30))
              + callout(8, 14, TL_TRACK_TOP + 144, ring=(12, TL_TRACK_TOP + 125, 348, 38))
              + callout(9, 14, TOOL_Y + 37, ring=(10, TOOL_Y + 6, 344, 62)),
    "split": lambda: editor(segs=SPLIT_SEGS, playhead=0.47, subs=(), speed_badge="", time="1:11.0", total="2:31.0", transitions=False)
             + callout(1, 16 + 340 * 0.47 + 18, TL_TRACK_TOP - 14, ring=(16 + 340 * 0.47 - 12, TL_TRACK_TOP - 14, 24, 100))
             + callout(2, TOOL_X[0] + 34, TOOL_Y + 4, ring=tool_ring(0)),
    "delete": lambda: editor(segs=DEL_SEGS, selected_deleted=True, show_deleted=True, speed_badge="", total="0:38.7", transitions=False)
              + callout(1, 16 + 340 * 0.51, TL_TRACK_TOP - 16, ring=(16 + 340 * 0.36, TL_TRACK_TOP, 340 * 0.30, 84))
              + callout(2, TOOL_X[1] + 34, TOOL_Y + 4, ring=tool_ring(1))
              + callout(3, 60, TL_TRACK_TOP + 150, ring=(20, TL_TRACK_TOP + 128, 40, 40)),
    "speed": speed_sheet,
    "subtitle-add": lambda: subtitle_dialog(False),
    "subtitle-edit": lambda: subtitle_dialog(True),
    "subtitles-timeline": lambda: editor(subtitle_on_preview="Take-off from Lysá hora", speed_badge="", playhead=0.2)
                          + callout(1, 16 + 340 * 0.19, TL_TRACK_TOP + 106, ring=(16 + 340 * 0.08 - 4, TL_TRACK_TOP + 86, 340 * 0.22 + 8, 36))
                          + callout(2, TOOL_X[3] + 34, TOOL_Y + 4, ring=tool_ring(3)),
    "transition-buttons": lambda: editor(transition_set=(1,))
                          + callout(1, 16 + 340 * 0.36, TL_TRACK_TOP + 14, ring=(16 + 340 * 0.36 - 18, TL_TRACK_TOP + 24, 36, 36))
                          + callout(2, 34, TL_TRACK_TOP + 14, ring=(16, TL_TRACK_TOP + 24, 36, 36)),
    "transition": transition_dialog,
    "segment-info": segment_info,
    "export": export_sheet,
    "export-progress": export_running,
    "export-done": export_done,
    "missing-video": missing_video,
}


def main(names=None):
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SCREENS.items():
        if names and name not in names:
            continue
        svg = phone(fn())
        cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, f"{name}.png"), output_width=W * 2, output_height=H * 2)
        print("wrote", name)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
