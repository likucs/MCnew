import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_TEXT ="""<b>Hᴇʏ  ɪᴀᴍ ᴛᴇsᴛ ʙᴏᴛ ᴇᴘᴘᴏʟᴇ ᴘɪɴᴀ ᴇɴᴛʜɪɴᴀ ɴɪʟᴋɴᴇ ᴘᴏʏɪᴋᴏᴅᴇ ᴀᴘᴘᴀᴍ ʙʏᴇ</b>
"""
HELP_TEXT = """hey bruhh I can't help you so goway
"""
ABOUT_TEXT ="""<b>Lɪssᴀ ᴛᴇsᴛ Bᴏᴛ</b>
<b>🤷 DᴇᴠᴇLᴏᴘᴇʀ :- <a href="https://t.me/Xxxtentacion_TG">Xxxtentacion_TG</a></b>
<b>♞ Support: <a href="https://t.me/cinemazilla">cinemazilla</a></b>
<b>♞ Library: <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a></b>
<b>~ @no_ones_like_me</b>"""

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
                InlineKeyboardButton("𝘾𝙍𝙀𝘼𝙏𝙊𝙍", url="https://t.me/link"),
                InlineKeyboardButton("⚙ 𝙃𝙀𝙇𝙋", callback_data="help"),
            ],[
                InlineKeyboardButton("𝘾𝙇𝙊𝙎𝙀", callback_data="close"),
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
                InlineKeyboardButton("𝙂𝙊 𝘽𝘼𝘾𝙆", callback_data="start"),
                InlineKeyboardButton("𝘾𝙇𝙊𝙎𝙀", callback_data="close"),
            ],[
                InlineKeyboardButton("GROUP", url="https://t.me/CINEMAZILLA")
            ]]
           )        
          )

# for CallbackQuery
@Peaky.on_callback_query(filters.regex(r"^(start|help|about|close)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [[
            InlineKeyboardButton('CREATOR👤', url='https://t.me/PEAKY_BLINDER_TG'),
            InlineKeyboardButton('GROUP👥 🧾', url ='https://t.me/MGMOVIEGRAM')
        ],[
            InlineKeyboardButton('CHANNEL 🛠', url='https://t.me/MG_MEDIA')
        ],[
            InlineKeyboardButton('Help ⚙', callback_data="help")
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            START_TEXT,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "help":
        buttons = [[
            InlineKeyboardButton('Home ⚡', callback_data='start'),
            InlineKeyboardButton('About 🚩', callback_data='about')
        ],[
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            HELP_TEXT,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "about": 
        buttons = [[
            InlineKeyboardButton('Home ⚡', callback_data='start'),
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )


    elif query_data == "close":
        await update.message.delete()
Peaky.run()
