
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

SONG_TEXT = """<b>🎧 𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚃𝙾 𝙼𝙿3 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁 𝙱𝙾𝚃 

𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 𝚆𝙸𝚃𝙷 /song 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 🎧</b>"""

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

SOURCE_TEXT = """<b>എന്നെ കൊണ്ട് ചെയ്യാൻ കഴിയുന്ന കുറച്ചു കാര്യങ്ങൾ ആണ് താഴേ കൊടുത്തിട്ടുള്ളത്..</b>"""
TELEGRAPH_TEXT = """<b>🔗 𝙸 𝙲𝙰𝙽 𝚄𝙿𝙻𝙾𝙰𝙳 𝙿𝙷𝙾𝚃𝙾𝚂 𝙰𝙽𝙳 𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝚃𝙴𝙻𝙶𝚁𝙰𝙿𝙷. 

𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 🔗</b>"""
INFO_TEXT = """<b>☆ 𝙸𝙵 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝙰 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 𝙸𝙳 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙷𝙴𝚁𝙴 [ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ]

☆ 𝙸𝙵 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳 𝙲𝙻𝙸𝙲𝙺 /stickerid 𝚃𝙾 𝙶𝙴𝚃  𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳

☆ 𝙲𝙻𝙸𝙲𝙺 /info 𝚃𝙾 𝙿𝙸𝙲𝙺 𝚄𝙿 𝚈𝙾𝚄𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽

☆ 𝙸𝙵 𝚈𝙾𝚄 𝚂𝙴𝙽𝙳 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 [ᴜsɪɴɢ ᴛʜᴇ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ] 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚁 [ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴛᴇ] 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝚈𝙾𝚄𝚁 𝙸𝙳 𝙾𝙵 𝚃𝙷𝙰𝚃 𝙶𝚁𝙾𝚄𝙿 𝙾𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b>"""


@Client.on_callback_query(filters.regex(r"^(start|help|about|close|home|song|Telegraph|info)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [
                     [
                    InlineKeyboardButton("🔎 𝚈𝚃 𝚂𝙴𝙰𝚁𝙲𝙷", switch_inline_query_current_chat='')
                    ],[
                    InlineKeyboardButton("⚠️ 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/cinemazilla"),
                    InlineKeyboardButton("🕵‍♂ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁", url="https://t.me/peaky_blinder_tg"),
                    ],[
                    InlineKeyboardButton("💡 𝙷𝙴𝙻𝙿", callback_data="help"),
                    InlineKeyboardButton("♻️ 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂", callback_data="home"),
                    ]
                 ]
    
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
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close'),
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

    elif query_data == "home": 
        buttons = [[
            InlineKeyboardButton('🎧 𝚂𝙾𝙽𝙶', callback_data='song'),
            InlineKeyboardButton('🔗 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙿𝙷', callback_data='Telegraph'),
        ],[
            InlineKeyboardButton('📅 𝙸𝙽𝙵𝙾', callback_data='info'),
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺 ', callback_data='start'),
        ]]

        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            SOURCE_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "song": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            SONG_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "Telegraph": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            TELEGRAPH_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "info": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            INFO_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "close":
        await update.message.delete()

    elif query_data == "song_ex":
        await update.answer("""𝗘𝗫𝗔𝗠𝗣𝗟𝗘𝗦 :

/song no idea ✅
No idea ❌

/song fadded ✅
fadded ❌""", show_alert=True))
