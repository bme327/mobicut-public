# mobiCut — public repository

**The documentation moved to https://bmesoft.eu/mobicut/docs/** (Czech:
https://bmesoft.eu/cs/mobicut/docs/). It is now part of the bmesoft.eu website, built in the
mobiCut app repository.

This repository still holds:

- **Release notes**: each app release gets a GitHub release here with a one-line note and no files
  (the app's *What's new* opens https://github.com/bme327/mobicut-public/releases/latest).
- **Issues**: bug reports and feature requests (see the docs' Feedback page).
- **Redirects**: GitHub Pages still serves https://bme327.github.io/mobicut-public/, because
  installed apps link to it. Every old page (`index.md`, `operations/*.md`, `cs/…`) is only front
  matter with `redirect_to:` its new address (plugin `jekyll-redirect-from`). Keep them for good;
  the PR check builds the site and checks that every page redirects to bmesoft.eu.

There is no public APK download. The app is planned for Google Play in mid-November 2026.
