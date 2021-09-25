
import re
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

START_TEXT ="""<b>Nᴏᴡ ᴀᴠᴀɪʟᴀʙʟᴇ Cᴍᴅs :
⍟ I ᴄᴀɴ Uᴘʟᴏᴀᴅ Pʜᴏᴛᴏs Oʀ Vɪᴅᴇᴏs Tᴏ Tᴇʟᴇɢʀᴀᴘʜ
⍟ /song - ᴇx (/song no idea)
⍟/info - Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ</b>"""

HELP_TEXT = """<b>Nᴏᴡ ᴀᴠᴀɪʟᴀʙʟᴇ Cᴍᴅs :
⍟ I ᴄᴀɴ Uᴘʟᴏᴀᴅ Pʜᴏᴛᴏs Oʀ Vɪᴅᴇᴏs Tᴏ Tᴇʟᴇɢʀᴀᴘʜ
⍟ /song - ᴇx (/song no idea)
⍟/info - Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ</b>"""

CALLBACK_TEXT = """<b>𝙷𝙴𝚈 𝙸𝙰𝙼 𝙹𝚄𝚂𝚃 𝚃𝙴𝚂𝚃 𝙾𝙵 𝙿𝙴𝙰𝙺𝚈 𝙱𝙻𝙸𝙽𝙳𝙴𝚁 </b>"""

ABOUT_TEXT ="""<b>Nᴀᴍᴇ :-<b>Lɪssᴀ ᴛᴇsᴛ Bᴏᴛ</b>
<b>⍟ DᴇᴠᴇLᴏᴘᴇʀ :- <a href="https://t.me/Xxxtentacion_TG">Xxxtentacion_TG</a></b>
<b>⍟ Credits :- Everyone in this journey</b>
<b>⍟ Server :-<a href="https://herokuapp.com/">Hᴇʀᴏᴋᴜ</a></b>
<b>⍟ source code :- <a href="https://t.me/AdhavaaBiriyaniKittiyalo">Cʟɪᴄᴋ ʜᴇʀᴇ</a></b>
<b>⍟ Library: <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a></b>
<b>~ @no_ones_like_me</b>"""


@Client.on_callback_query(filters.regex(r"^(start|help|about|close|alert|sourcecode)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [[
            InlineKeyboardButton('👨‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url='https://t.me/PEAKY_BLINDER_TG'),
            InlineKeyboardButton('🔰 𝙶𝚁𝙾𝚄𝙿', url ='https://t.me/cinemazilla')
        ],[
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data="close"),
            InlineKeyboardButton('⚙ Help', callback_data="help"),
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            CALLBACK_TEXT.format(update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "help":
        buttons = [[
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start'),
            InlineKeyboardButton('🤖 𝙰𝙱𝙾𝚄𝚃', callback_data='about')
        ],[
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
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
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start'),
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )
       await update.message.edit_text(
            CALLBACK_TEXT.format(update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "sourcecode":
        buttons = [[
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start'),
            InlineKeyboardButton('🤖 𝙰𝙱𝙾𝚄𝚃', callback_data='about')
        ],[
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)


    elif query_data == "close":
        await update.message.delete()
    elif query_data == "alert":
        await update.answer("കൌതുകും ലേശം കൂടുതൽ ആണല്ലേ👀",show_alert=True)
