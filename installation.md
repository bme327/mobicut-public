---
title: Installation
nav_order: 2
---

# Installation
{: .no_toc }

Until mobiCut is on Google Play, it is installed from an **APK file**, the Android app package.
Every new build of the app is published automatically, and one fixed link always points to the
newest one.

1. TOC
{:toc}

---

## Before you start

- A phone with **Android 10 or newer**.
- About 70 MB free for the download and the app, plus room for the videos you export.
- Permission to install apps from your browser (Android asks for this the first time, see below).

## Install the latest build

1. **On the phone**, open this link in your browser (Chrome, Firefox, …):

   [**Download the latest mobiCut APK**]({{ site.apk_url }}){: .btn .btn-primary }

   {% include downloads.html %}

   The file is called `mobicut.apk` (about 65 MB). All builds are also listed on the
   [releases page](https://github.com/bme327/mobicut-public/releases).

2. When the download finishes, tap **Open** in the notification or the browser's download bar.
   You can also find it later in the **Files** app under **Downloads**.

3. The first time, Android says that your browser isn't allowed to install apps.
   Tap **Settings**, turn on **Allow from this source**, and go back.

4. Tap **Install**.

5. If **Google Play Protect** warns that it doesn't recognise the app, tap **More details →
   Install anyway**. This appears because the build isn't from the Play Store yet.

6. Tap **Open**. mobiCut starts on the project list, which is empty the first time.

{% include screen.html name="home-empty" alt="mobiCut's start screen with no projects: 'No projects yet' and a New project button." caption="First start: no projects yet." %}

## Updating

Open the same link again and install. **A new build installs over the old one and keeps all your
projects**, because every build is signed with the same key.

{: .warning }
> Don't uninstall mobiCut to update it. Uninstalling deletes your projects (your edits). Your
> original videos and exported videos stay in the gallery either way.

To see which build you have, open **⚙ Settings** on the start screen; the version is shown at
the bottom (for example *mobiCut {{ site.app_version }}*).

## Uninstalling

Long-press the mobiCut icon → **App info** → **Uninstall**. This removes the app and its
projects. Videos you exported stay in `Movies/MobiCut`, subtitle files in `Download/MobiCut`.

## Troubleshooting

| What you see | What to do |
|---|---|
| *App not installed* / *package conflicts with an existing package* | A build signed differently is already installed (rare). Uninstall it first. This loses its projects. |
| *There was a problem parsing the package* | The download didn't finish. Delete `mobicut.apk` from Downloads and download it again. |
| The **Install** button does nothing | Close other apps that draw over the screen (bubbles, screen dimmers) and try again. |

Something else? [Report a bug]({{ "/feedback/" | relative_url }}) with a screenshot of your version and the steps that lead to it.
