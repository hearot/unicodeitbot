#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is a part of unicodeitbot
#
# Copyright (c) 2020 Hearot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
unicodeitbot - Converts LaTeX tags
to unicode using an inline Telegram
bot jointly with unicodeit.
"""

import argparse
import logging

import ujson as json
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                      InlineQueryResultArticle, InputTextMessageContent,
                      ParseMode, Update)
from telegram.ext import (CommandHandler, Filters, InlineQueryHandler,
                          MessageHandler, Updater)
from unicodeit import replace

EXAMPLE = "\\forall z \\in \\mathbb{C}, \\exists -z s.t. z + (-z) = 0"
GITHUB_REPOSITORY = "https://github.com/hearot/unicodeitbot"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "⌨️ Try it in inline mode!", switch_inline_query_current_chat=EXAMPLE
            )
        ]
    ]
)


def inline_query(update: Update, _):
    """Translate LaTeX to unicode, then send it using the inline mode."""
    result = replace(update.inline_query.query).strip()

    if not result:
        return

    update.inline_query.answer(
        [
            InlineQueryResultArticle(
                id="result",
                title=result[:15] + "..." if len(result) > 15 else result,
                input_message_content=InputTextMessageContent(result),
            )
        ]
    )


def message(update: Update, _):
    """Translate LaTeX to unicode, then send it as a message."""
    update.message.reply_text(replace(update.message.text))


def start(update: Update, _):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        (
            "⌨️ Translate LaTeX to unicode by texting this "
            + "bot or using it in inline mode. See the source "
            + f'code on <a href="{GITHUB_REPOSITORY}">GitHub</a>.'
        ),
        parse_mode="HTML",
        reply_markup=keyboard,
    )


def main():
    """Start the bot."""
    parser = argparse.ArgumentParser(description=__doc__.rstrip())
    parser.add_argument(
        "-t", "--token", help="The Telegram bot token", required=True, type=str
    )
    parsed_arguments = parser.parse_args()

    logger.info(__doc__.rstrip())

    updater = Updater(parsed_arguments.token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(InlineQueryHandler(inline_query))
    updater.dispatcher.add_handler(MessageHandler(Filters.private, message))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
