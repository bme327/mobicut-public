---
title: Feedback
nav_order: 5
---

# Report a bug or suggest a feature

Feedback goes to [GitHub issues](https://github.com/bme327/mobicut-public/issues). You need a
free GitHub account.

[🐞 Report a bug](https://github.com/bme327/mobicut-public/issues/new?template=bug.yml){: .btn .btn-primary .mr-2 }
[💡 Suggest a feature](https://github.com/bme327/mobicut-public/issues/new?template=feature.yml){: .btn .mr-2 }
[👍 Vote on features](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement+sort%3Areactions-%2B1-desc){: .btn }

## Bug reports

The form asks for two things that make a bug fixable:

1. **A screenshot of your version.** On the start screen tap **⚙ Settings**; the version is at
   the bottom (for example *mobiCut {{ site.app_version }}*). Screenshot it and drop it into the
   form.

2. **Steps to reproduce**: exactly what you did, step by step, plus what you expected and what
   happened instead.

{% include screen.html name="settings-edition" alt="The Settings sheet; the app version is at the bottom." caption="Where to find the version: ⚙ Settings, at the bottom." %}

## Feature requests

Describe what you'd like mobiCut to do and what it would help you with.

### Voting

**Vote with a 👍 reaction** on the request (the smiley button under its description). The
[most wanted list](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement+sort%3Areactions-%2B1-desc)
is sorted by 👍, and that order helps decide what comes next. Please vote instead of opening a
duplicate, and don't add "+1" comments.

## What happens to a report or request

Every bug report and feature request carries exactly one status label, and moves through it like
this:

<div class="lifecycle">
  <span class="label label-grey">new</span> →
  <span class="label label-green">accepted</span> →
  <span class="label label-purple">closed</span>
  <span class="lc-or">or</span>
  <span class="label label-grey">new</span> →
  <span class="label label-red">rejected</span>
</div>


| Status | Meaning |
|---|---|
| <span class="label label-grey">status: new</span> | Not looked at yet |
| <span class="label label-green">status: accepted</span> | Planned for mobiCut; the issue stays open until it's released |
| <span class="label label-red">status: rejected</span> | Won't be done. The reason is in a comment, and the issue is closed as *not planned* |
| <span class="label label-purple">status: closed</span> | Fixed or done, and released. The comment says in which build; the issue is closed as *completed* |

A bug goes **new → accepted → closed** once a build with the fix is out (or **rejected**, for
example when it can't be reproduced). A feature request goes **new → accepted → closed** when it ships.

Closed and rejected issues stay readable. Search them before reporting, because the answer may
already be there: [closed bugs](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+label%3Abug+is%3Aclosed),
[rejected requests with reasons](https://github.com/bme327/mobicut-public/issues?q=is%3Aissue+label%3A%22status%3A+rejected%22).

{: .tip }
> When a bug you reported is **closed**, the closing comment names the build with the fix.
> [Update the app]({{ "/installation/#updating" | relative_url }}) to get it.
