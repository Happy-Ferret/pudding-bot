#!/usr/bin/env python
# pylint: disable=C0116,W0613

from telegram import BotCommand

Commands = {
    1: BotCommand("about", "About this bot."),
    2: BotCommand("id", "Reply to a message to get user ID.")
}

AdminCommands = {
    1: BotCommand("about", "About this bot."),
    2: BotCommand("id", "Reply to a message to get user ID."),
    3: BotCommand("mute", "Mute a user."),
    4: BotCommand("unmute", "Unmute a user."),
    5: BotCommand("ban", "Ban a user."),
    6: BotCommand("unban", "Unban a user."),
    7: BotCommand("pin", "Pin a message.")
}
