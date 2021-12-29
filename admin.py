#!/usr/bin/env python
# pylint: disable=C0116,W0613

from functools import wraps
from telegram import Update

def config_chat_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        update = args[2].to_dict() if not isinstance(args[2], dict) else args[2]
        chat_id = update['message']['chat']['id']
        if int(chat_id) != int(args[0].config.group_id):
            return
        f(*args, **kwargs)
    return wrapper


def admin_only(test: str):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(test)
        return wrapper
    return decorator


def exempt_admins():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            update = args[2].to_dict() if not isinstance(args[2], dict) else args[2]
            user_id = update['message']['from']['id']
            if user_id in args[0].config.admin_ids:
                return
            f(*args, **kwargs)
        return wrapper
    return decorator

def check_perm (update: Update):
    # Check user permission. Might be hard to generalize.
    # Maybe we need check_perm_pin() and others instead.
    # Or check_perm(update, perm: Type_CONST)
    bot = update.message.chat.bot
    chat = bot.get_chat(update.message.chat.id)
    user = update.message.from_user.id
    admin = chat.get_member(user)
    return (admin.status in ('administrator', 'creator'))

def check_admin(update: Update):
    bot = update.message.chat.bot
    chat = bot.get_chat(update.message.chat.id)
    user = update.message.from_user.id
    admin = chat.get_member(user)
    # if admin.status in ('administrator', 'creator') == True:
    return (admin.status in ('administrator', 'creator'))

    # admins = [
    #     f"@{admin.user.username}"
    #     for admin in chat.get_administrators()
    #     if admin.user.id != user
    #         pass
    #     else:
    # ]
    # admins = [
    #     f"@{admin.user.username}"
    #     for admin in chat.get_administrators()
    #     if admin.user.id != bot.get_me().id
    # ]
    # return False
