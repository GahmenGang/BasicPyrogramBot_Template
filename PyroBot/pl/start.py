# https://github.com/GahmenGang/

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from PyroBot import Bot

MESSAGE = (
        'Hello there!\n'
        'I am a Simple Bot Build with Pyrogram and Python\n\n'
        'By [GahmenGang](https://github.com/GahmenGang/)'
    )

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='Github', url='github.com/GahmenGang')],
    [InlineKeyboardButton(text='Source Code', url='github.com/GahmenGang/BasicPyrogramBot_Template')]]
)

@excmd.on_message(filters.text & filters.private & ~filters.bot)
async def start(sessionCli, message):
    await message.reply(
        text=MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=False
    )

