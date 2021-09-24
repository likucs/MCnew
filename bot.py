import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

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
                reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Buttton", url="https://t.me/link"),
                InlineKeyboardButton("Buttton", callback_data="help"),
            ],[
                InlineKeyboardButton("Buttton", url="https://t.me/link")
            ]]
           )        
          )

@Peaky.on_message(filters.command("help"))
async def help(client, message):
   if message.chat.type == 'private':
       await Peaky.send_message(
               chat_id=message.chat.id,
               text=START_TEXT,
                reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Buttton", url="https://t.me/link"),
                InlineKeyboardButton("Buttton", url="https://t.me/link")
            ],[
                InlineKeyboardButton("Buttton", url="https://t.me/link")
            ]]
           )        
          )

# for CallbackQuery
@Peaky.on_callback_query()
def Common(client, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    user_name = query.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    if data == "help":
        query.message.edit(f"your start message.",
        reply_markup = InlineKeyboardMarkup(
      [[
           InlineKeyboardButton("Buttton", url="https://t.me/link"),
           InlineKeyboardButton("Buttton", url="https://t.me/link")
      ],[
           InlineKeyboardButton("Buttton", url="https://t.me/link")
      ]]
    ))
Peaky.run()
