
import re
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Peaky.on_callback_query(filters.regex(r"^(start|help|about|close)$"), group=2)
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


    elif query_data == "close":
        await update.message.delete()
