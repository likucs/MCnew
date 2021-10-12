
import re
import time
import asyncio
import os
import ast

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from wasim_faris.filter_db import del_all, find_filter

from wasim_faris.connect_db import(
    all_connections,
    active_connection,
    if_active,
    delete_connection,
    make_active,
    make_inactive
)
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

START_TEXT ="""<b>Nᴏᴡ ᴀᴠᴀɪʟᴀʙʟᴇ Cᴍᴅs :
⍟ I ᴄᴀɴ Uᴘʟᴏᴀᴅ Pʜᴏᴛᴏs Oʀ Vɪᴅᴇᴏs Tᴏ Tᴇʟᴇɢʀᴀᴘʜ
⍟ /song - ᴇx (/song no idea)
⍟/info - Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ</b>"""
STRING_TEXT = """<b>String Session Generator</b>

<code>I Can Generate Pyrogram's String Session<code>

<code>just Click</code> <b>/string</b> <code>to generate String Session of your telegram</code>"""
SONG_TEXT = """<code>🎧 Iam a Simple YouTube To MP3 Downloader Bot 

Send Me Any Song Name With <b>/song</b> Command 🎧 </code>"""
WASIM_TEXT = """<code>Base Commands

👮🏻 Available to Admins&Moderators
🕵🏻 Available to Admins</code>"""

HELP_TEXT = """<b>നീ ഏതാ..... ഒന്ന് പോടെയ് അവൻ help ചോയ്ച്ച് വന്നിരിക്കുന്നു😤...I'm Different Bot U Know</b>"""

CALLBACK_TEXT = """<b>𝙷𝙴𝚈 𝙸𝙰𝙼 𝙹𝚄𝚂𝚃 𝚃𝙴𝚂𝚃 𝙾𝙵 𝙿𝙴𝙰𝙺𝚈 𝙱𝙻𝙸𝙽𝙳𝙴𝚁 </b>"""
DEVS_TEXT = """♻️ 𝙷𝙴𝚈  𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙳𝙴𝚅𝚂 ♻️"""
MUTE_TEXT = """<code> Here is the help for the Muting module:</code>

<code>Admin only:</code>
 - /mute <code><userhandle>: silences a user. Can also be used as a reply, muting the replied to user.</code>
 - /tmute <code><userhandle> x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.</code>
 - /unmute <code><userhandle>: unmutes a user. Can also be used as a reply, muting the replied to user<code>."""
BANS_TEXT = """<code>Here is the help for the Bans module:</code>

 - /kickme: <code>kicks the user who issued the command</code>

<code>Admin only:
 - /ban <code><userhandle>: bans a user. (via handle, or reply)</code>
 - /tban <code><userhandle> x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.</code>
 - /unban <code><userhandle>: unbans a user. (via handle, or reply)</code>
 - /kick <code><userhandle>: kicks a user, (via handle, or reply)</code>"""

ABOUT_TEXT ="""<code>★ My name  :- Lissa Bot</code>
<b>★Developer :- <a href="https://t.me/Xxxtentacion_TG">xxxtentacion</a></b>
<code>★ Credits :- Every One In This Journey</code>
<b>★ Server :- <a href="https://herokuapp.com/">Heroku</a></b>
<b>★ Source Code :- <a href="https://t.me/AdhavaaBiriyaniKittiyalo">Click here</a></b>
<b>★ Library :- <a href="https://github.com/pyrogram/pyrogram">pyrogram</a></b>"""

SOURCE_TEXT = """<b>എന്നെ കൊണ്ട് ചെയ്യാൻ കഴിയുന്ന കുറച്ചു കാര്യങ്ങൾ ആണ് താഴേ കൊടുത്തിട്ടുള്ളത്..</b>"""
TELEGRAPH_TEXT = """<code>⛓ I can Upload Photo And Video To Telegraph 

Send me Any  Photo or Video 
 /telegraph With telegraph  Command (reply with photo or video) </code>

<b>CMD /telegraph</b>"""
INFO_TEXT = """<b>Cmd /info, /stickerid</b>

<code>☆ If You Need a Telegram User Id Forword A message To Here ( With forward tag )

If You Need Telegram Sticker Id Click /stickerid To Get Sticker Id ( Reply With Sticker )

☆ Click /info To Pick Up Your Telegram Information

☆ If You Send a message ( Using Forward Tag ) From Your ( Public Or private ) Group and channnel You Will Receive Your Id Of That Group Or Channel</code>"""

FILTER_TEXT = """ <b>Help for Filter</b>

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾𝗌:</b>

• /add <code>- 𝖺𝖽𝖽 a filter</code>
• /view <code>- list all the filters of a chat.</code>
• /connect - <code>connect your group</code>
• /delfilter <code>- delete a specific filter.</code>
• /delall_filters <code>- deletes whole filters of a chat.</code>"""

CORONA_TEXT ="""<b>Here is the help for the coron information module</b>

<b>/covid  <country name></b><code> you can find a corona information of every country 

example : - /covid india</code>"""

@Client.on_callback_query(filters.regex(r"^(start|help|about|close|home|song|Telegraph|info|song_ex|devs|ban|mute|bans|delallconfirm|delallcancel|string|filter|coronainfo)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [
                [
                    InlineKeyboardButton("➕ Add Me To Your Group ➕", url="t.me/Lissa_test_bot?startgroup=true"),
                ],[
                    InlineKeyboardButton("🕵‍♂ Creator", callback_data="devs"),
                    InlineKeyboardButton("⚠️ Group", url="https://t.me/peaky_blinder_tg"),
                ],[
                    InlineKeyboardButton("💡 Help", callback_data="home"),
                    InlineKeyboardButton("😃 About", callback_data="about"),
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
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close'),
            InlineKeyboardButton('♻️', callback_data='about')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "home": 
        buttons = [[
            InlineKeyboardButton('Song', callback_data='song'),
            InlineKeyboardButton('Telegraph', callback_data='Telegraph'),
            InlineKeyboardButton('Info', callback_data='info'),
        ],[
            InlineKeyboardButton('String Gen', callback_data='string'),
            InlineKeyboardButton('Mute', callback_data='mute'),
            InlineKeyboardButton('Ban', callback_data='bans'),   
        ],[
            InlineKeyboardButton('Filter', callback_data='filter'),
            InlineKeyboardButton('Corona', callback_data='bans'),
            InlineKeyboardButton('Country', callback_data='bans'),
        ],[
            InlineKeyboardButton('Google Search', callback_data='bans'),
            InlineKeyboardButton('Extra', callback_data='bans'),
            InlineKeyboardButton('Memes', callback_data='bans'),
        ],[
            InlineKeyboardButton('ytdl', callback_data='bans'),
            InlineKeyboardButton('Pin', callback_data='bans'),
            InlineKeyboardButton('font', callback_data='bans'),
        ],[
            InlineKeyboardButton('calculator', callback_data='bans'),
            InlineKeyboardButton('img to pdf', callback_data='bans'),
            InlineKeyboardButton('◀️ Back', callback_data='start'),
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
            InlineKeyboardButton('❓ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴𝚂', callback_data='song_ex')
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

    elif query_data == "devs": 
        buttons = [[
            InlineKeyboardButton('♻️ 1 𝙳𝙴𝚅', url="https://t.me/Peaky_blinder_tg"),
            InlineKeyboardButton('♻️ 2 𝙳𝙴𝚅', url="https://t.me/Xxxtentacion_TG")
        ],[
            InlineKeyboardButton('♻️ 3 𝙳𝙴𝚅', url="https://t.me/THEREALMR_JINN_OF_TG"),
            InlineKeyboardButton('𝙱𝙰𝙲𝙺 ▶️', callback_data='start'),
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            DEVS_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "ban": 
        buttons = [[
            InlineKeyboardButton('😐 𝙼𝚄𝚃𝙴', callback_data='mute'),
            InlineKeyboardButton('🚫 𝙱𝙰𝙽', callback_data='bans')
        ],[
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start'),
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            WASIM_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "mute": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            MUTE_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "bans": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            BANS_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )

    elif query_data == "string": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            STRING_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )
    elif query_data == "filter": 
        buttons = [[
            InlineKeyboardButton('◀️ 𝙱𝙰𝙲𝙺', callback_data='home'),
            InlineKeyboardButton('🏘 𝙷𝙾𝙼𝙴', callback_data='start')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            FILTER_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )
    elif query_data == "coronainfo": 
        buttons = [[
            InlineKeyboardButton('◀️ back', callback_data='home'),
            InlineKeyboardButton('🏘 home', callback_data='start')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            CORONA_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )


    elif query_data == "close":
        await update.message.delete()

    elif query_data == "song_ex":
        await update.answer("𝗘𝗫𝗔𝗠𝗣𝗟𝗘𝗦 :\n\n/song no idea ✅\nNo idea ❌\n\n/song fadded ✅\nfadded ❌", show_alert=True)

    
