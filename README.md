# mobiCut — public documentation

User documentation for **mobiCut**, a small video editor for Android, published with GitHub Pages.

- Site: https://bme327.github.io/mobicut-public/
- Install the app: https://github.com/bme327/mobicut-public/releases/latest/download/mobicut.apk

## Layout

| Path | What |
|---|---|
| `index.md` | Intro: what mobiCut is, editions (Free / Pro) |
| `installation.md` | Installing and updating from the APK |
| `operations/*.md` | One page per operation |
| `assets/screens/*.png` | Drawn screen illustrations (generated) |
| `assets/screens/real/*.png` | Real phone screenshots; a file here replaces the illustration with the same name |
| `_tools/screens.py` | Draws the illustrations from the app's UI (colors and labels from its Compose code) |
| `_config.yml` | Theme, `apk_url`, `app_version` |
| `cs/` | Czech translation: the same paths under `cs/` (`cs/installation.md` ↔ `installation.md`) |

Regenerate illustrations: `pip install cairosvg && python3 _tools/screens.py`

## Real screenshots

Take a screenshot on the phone, crop to the app (portrait; the `tablet-*` screens are a tablet in
landscape), and save it as
`assets/screens/real/<name>.png` using the same name as the illustration (e.g. `editor.png`).
The page switches to it automatically.

## Languages

Every page exists twice: English at `x.md` (URL `/x/`) and Czech at `cs/x.md` (URL `/cs/x/`).
**When a page is added or changed, change its twin too.**

- `page.lang` comes from `_config.yml` defaults (`cs/` → `cs`, everything else → `en`). The
  sidebar shows only the current language (`_includes/components/site_nav.html`, `sidebar.html`,
  `breadcrumbs.html`, `children_nav.html` are theme copies that pass `lang`), and
  `_includes/header_custom.html` links each page to its twin.
- Czech child pages use `parent: Funkce` (the Czech title of Operations).
- Keep heading anchors the same in both languages: Czech headings carry the English id,
  e.g. `## Odinstalace {#uninstalling}`, so `#…` links work in both.
- The app's UI is English, so button and screen names stay in English (bold) on Czech pages.
  Screens and illustrations are shared (English); only their alt text is translated.
