import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT ="hey iam simpler bot"

Peaky = Client(
   "Lisa_bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Peaky.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Peaky.send_message(
               chat_id=message.chat.id,
               text=START_TEXT,
               parse_mode="html"
               reply_markup=InlineKeyboardMarkup(
            [
              [
                  InlineKeyboardButton("Buttton", url="https://t.me/link"),
                  InlineKeyboardButton("Buttton", url="https://t.me/link")
              ],
              [
                 InlineKeyboardButton("Buttton", url="https://t.me/link")
              ]
           ]
          )        
         )
Peaky.run()
