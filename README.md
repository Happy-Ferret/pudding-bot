![Activity Level](https://img.shields.io/badge/status-active-brightgreen.svg?style=flat-square)
![Stability](https://anima-os.github.io/stabl-badges/experimental.svg)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=PuddingBot_pudding-bot&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=PuddingBot_pudding-bot)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=PuddingBot_pudding-bot&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=PuddingBot_pudding-bot)

<img src="profile.jpg" width="50%">

Pudding
===

Welcome to [@PuddingBot](https://t.me/puddingbot), my AGPL3 licensed group management bot.

More information and a [Docusaurus](https://docusaurus.io/docs) powered manual will be added at a later date.


## Why not just use Rose?

There are certain things bothering me about the design philosophy of Rose that I seek to avoid.

- It's closed source.

- Rose never warns that a filter has already been set, instead replacing it silently.

- Rose's anti-flooding is broken. It doesn't allow an admin to set the time frame between messages that are considered flooding, and the default setting isn't sensible.

- "Disables" are non-admin only. There should be a functionality to disable parts of the bot entirely.

- No way to query the reason a user was banned/muted. Rose support suggests running a log channel for that, which is additional hassle.

- Some other gimmicks like conveniently displaying a chat's basic information (title, description, ID, @ and invite link) or querying the bot's uptime are
absent.