
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

SONG_TEXT = """<b>🎧 𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚃𝙾 𝙼𝙿3 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁 𝙱𝙾𝚃 

𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 𝚆𝙸𝚃𝙷 /song 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 🎧</b>"""
WASIM_TEXT = """<b>Base Commands

👮🏻 Available to Admins&Moderators
🕵🏻 Available to Admins</b>"""

HELP_TEXT = """<b>നീ ഏതാ..... ഒന്ന് പോടെയ് അവൻ help ചോയ്ച്ച് വന്നിരിക്കുന്നു😤...I'm Different Bot U Know</b>"""

CALLBACK_TEXT = """<b>𝙷𝙴𝚈 𝙸𝙰𝙼 𝙹𝚄𝚂𝚃 𝚃𝙴𝚂𝚃 𝙾𝙵 𝙿𝙴𝙰𝙺𝚈 𝙱𝙻𝙸𝙽𝙳𝙴𝚁 </b>"""
DEVS_TEXT = """♻️ 𝙷𝙴𝚈  𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙳𝙴𝚅𝚂 ♻️"""
MUTE_TEXT = """<b>Here is the help for the Muting module:

Admin only:
 - /mute <userhandle>: silences a user. Can also be used as a reply, muting the replied to user.
 - /tmute <userhandle> x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
 - /unmute <userhandle>: unmutes a user. Can also be used as a reply, muting the replied to user.</b>"""
BANS_TEXT = """<b>Here is the help for the Bans module:

 - /kickme: kicks the user who issued the command

Admin only:
 - /ban <userhandle>: bans a user. (via handle, or reply)
 - /tban <userhandle> x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
 - /unban <userhandle>: unbans a user. (via handle, or reply)
 - /kick <userhandle>: kicks a user, (via handle, or reply)</b>"""

ABOUT_TEXT ="""<b>★ 𝙼𝚈 𝙽𝙰𝙼𝙴 :- 𝙻𝙸𝚂𝚂𝙰 𝙱𝙾𝚃</b>
<b>★ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 :- <a href="https://t.me/Xxxtentacion_TG">𝚇𝚇𝚇𝚃𝙴𝙽𝚃𝙰𝙲𝚃𝙸𝙾𝙽_𝚃𝙶</a></b>
<b>★ 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 :- 𝙴𝚅𝙴𝚁𝚈 𝙾𝙽𝙴 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙹𝙾𝚄𝚁𝙽𝙴𝚈</b>
<b>★ 𝚂𝙴𝚁𝚅𝙴𝚁 :- <a href="https://herokuapp.com/">𝙷𝙴𝚁𝙾𝙺𝚄</a></b>
<b>★ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 :- <a href="https://t.me/AdhavaaBiriyaniKittiyalo">𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a></b>
<b>★ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 :- <a href="https://github.com/pyrogram/pyrogram">𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a></b>"""

SOURCE_TEXT = """<b>എന്നെ കൊണ്ട് ചെയ്യാൻ കഴിയുന്ന കുറച്ചു കാര്യങ്ങൾ ആണ് താഴേ കൊടുത്തിട്ടുള്ളത്..</b>"""
TELEGRAPH_TEXT = """<b>🔗 𝙸 𝙲𝙰𝙽 𝚄𝙿𝙻𝙾𝙰𝙳 𝙿𝙷𝙾𝚃𝙾𝚂 𝙰𝙽𝙳 𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝚃𝙴𝙻𝙶𝚁𝙰𝙿𝙷. 

𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 🔗</b>"""
INFO_TEXT = """<b>☆ 𝙸𝙵 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝙰 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚄𝚂𝙴𝚁 𝙸𝙳 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙷𝙴𝚁𝙴 [ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ]

☆ 𝙸𝙵 𝚈𝙾𝚄 𝙽𝙴𝙴𝙳 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳 𝙲𝙻𝙸𝙲𝙺 /stickerid 𝚃𝙾 𝙶𝙴𝚃  𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳

☆ 𝙲𝙻𝙸𝙲𝙺 /info 𝚃𝙾 𝙿𝙸𝙲𝙺 𝚄𝙿 𝚈𝙾𝚄𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽

☆ 𝙸𝙵 𝚈𝙾𝚄 𝚂𝙴𝙽𝙳 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 [ᴜsɪɴɢ ᴛʜᴇ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ] 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚁 [ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴛᴇ] 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝚈𝙾𝚄𝚁 𝙸𝙳 𝙾𝙵 𝚃𝙷𝙰𝚃 𝙶𝚁𝙾𝚄𝙿 𝙾𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b>"""


@Client.on_callback_query(filters.regex(r"^(start|help|about|close|home|song|Telegraph|info|song_ex|devs|ban|mute|bans|delallconfirm|delallcancel)$"), group=2)
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
            InlineKeyboardButton('🚫 𝚁𝙴𝚂𝚃𝚁𝙸𝙲𝚃', callback_data='ban'),
        ],[
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

    elif query_data == "close":
        await update.message.delete()

    elif query_data == "song_ex":
        await update.answer("𝗘𝗫𝗔𝗠𝗣𝗟𝗘𝗦 :\n\n/song no idea ✅\nNo idea ❌\n\n/song fadded ✅\nfadded ❌", show_alert=True)

     elif query_data == "wasimh":
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        act = query.data.split(":")[3]
        user_id = query.from_user.id

        if act == "":
            stat = "CONNECT"
            cb = "connectcb"
        else:
            stat = "DISCONNECT"
            cb = "disconnect"

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{stat}", callback_data=f"{cb}:{group_id}:{title}"),
                InlineKeyboardButton("DELETE", callback_data=f"deletecb:{group_id}")],
            [InlineKeyboardButton("BACK", callback_data="backcb")]
        ])

        await query.message.edit_text(
            f"Group Name : **{title}**\nGroup ID : `{group_id}`",
            reply_markup=keyboard,
            parse_mode="md"
        )
        return

    elif "connectcb" in query.data:
        await query.answer()

        group_id = query.data.split(":")[1]
        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkact = await make_active(str(user_id), str(group_id))

        if mkact:
            await query.message.edit_text(
                f"Connected to **{title}**",
                parse_mode="md"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return

    elif "disconnect" in query.data:
        await query.answer()

        title = query.data.split(":")[2]
        user_id = query.from_user.id

        mkinact = await make_inactive(str(user_id))

        if mkinact:
            await query.message.edit_text(
                f"Disconnected from **{title}**",
                parse_mode="md"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return
    elif "deletecb" in query.data:
        await query.answer()

        user_id = query.from_user.id
        group_id = query.data.split(":")[1]

        delcon = await delete_connection(str(user_id), str(group_id))

        if delcon:
            await query.message.edit_text(
                "Successfully deleted connection"
            )
            return
        else:
            await query.message.edit_text(
                f"Some error occured!!",
                parse_mode="md"
            )
            return
    
    elif query.data == "backcb":
        await query.answer()

        userid = query.from_user.id

        groupids = await all_connections(str(userid))
        if groupids is None:
            await query.message.edit_text(
                "There are no active connections!! Connect to some groups first.",
            )
            return
        buttons = []
        for groupid in groupids:
            try:
                ttl = await client.get_chat(int(groupid))
                title = ttl.title
                active = await if_active(str(userid), str(groupid))
                if active:
                    act = " - ACTIVE"
                else:
                    act = ""
                buttons.append(
                    [
                        InlineKeyboardButton(
                            text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                        )
                    ]
                )
            except:
                pass
        if buttons:
            await query.message.edit_text(
                "Your connected group details ;\n\n",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    elif "alertmessage" in query.data:
        grp_id = query.message.chat.id
        i = query.data.split(":")[1]
        keyword = query.data.split(":")[2]
        reply_text, btn, alerts, fileid = await find_filter(grp_id, keyword)
        if alerts is not None:
            alerts = ast.literal_eval(alerts)
            alert = alerts[int(i)]
            alert = alert.replace("\\n", "\n").replace("\\t", "\t")
            await query.answer(alert,show_alert=True)

