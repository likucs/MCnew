import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT ="""hey iam simpler bot"""

Peaky = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Peaky.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Peaky.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot
I can upload photos or videos to telegraph. Made by <a href="https://t.me/peaky_blinder_tg">[★] ᴘᴇᴀᴋʏ вℓιи∂єя [★]</a>
Hit help button to find out more about how to use me</b>""",  
