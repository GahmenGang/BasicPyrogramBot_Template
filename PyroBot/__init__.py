# https://github.com/GahmenGang/

from pyrogram import Client
from pyromod import listen
import logging

from config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Client
Bot = Client(
    'PyroBot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(
        root='PyroBot.pl'
    )
)
