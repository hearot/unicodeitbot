# [unicodeitbot](https://t.me/unicodeitbot)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE) [![Developer: @hearot](https://img.shields.io/badge/Developer-%20@hearot-red.svg)](https://t.me/hearot)

Converts LaTeX tags to unicode using an inline Telegram bot jointly with [unicodeit](https://github.com/svenkreiss/unicodeit).

To run the bot yourself, you will need:
- Python (tested with 3.8).
- The [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) module.
- The [unicodeit](https://github.com/svenkreiss/unicodeit) module.

## Setup
- Get a token from [BotFather](http://t.me/BotFather).
- Activate the *Inline mode* using the `/setinline` command with [BotFather](http://t.me/BotFather).
- Install the requirements (using `virtualenv` is recommended) using `pip install -r requirements.txt`
- Then, you can run the bot using `python bot.py -t BOT_TOKEN`.
