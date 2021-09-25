import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import logging
from pyrogram import Client, filters
from config import Config
import random

PHOTOS = [
    "https://telegra.ph/file/b4d4c014012f3c31552ed.jpg",
    "https://telegra.ph/file/0f1aa03b2162f77871c47.jpg",
    "https://telegra.ph/file/ecc38a0406adf3ee5ac47.jpg",
    "https://telegra.ph/file/1ca922556aab3c70d6365.jpg",
    "https://telegra.ph/file/a596e2b2bc792c0b70777.jpg",
    "https://telegra.ph/file/aab5d709b5d269bf08e32.jpg",
    "https://telegra.ph/file/a94fbf80d6e482486e754.jpg",
    "https://telegra.ph/file/da728cfae93e363b02285.jpg",
    "https://telegra.ph/file/2720d4e5860f464ff7af6.jpg",
    "https://telegra.ph/file/14e1badc41205ac7401ee.jpg",
    "https://telegra.ph/file/22ff59822ed4eb5f4bf12.jpg",
    "https://telegra.ph/file/05f56fbc072cbf452e786.jpg",
    "https://telegra.ph/file/be2d1988dad28d3623741.jpg",
    "https://telegra.ph/file/409880ce7409a7f08cc67.jpg",
    "https://telegra.ph/file/81653df06e7efcb354af9.jpg",
    "https://telegra.ph/file/4a66e753a81e7fe216467.jpg",
    "https://telegra.ph/file/c287c1ec90b6a9876fa73.jpg",
    "https://telegra.ph/file/fe47bf785fc127335ac1f.jpg",
]


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

API = "https://apibu.herokuapp.com/api/y-images?query="

Peaky = Client(
   "Lisa_bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
   plugins=dict(root="plugins")
)

@Peaky.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    await update.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ <a href="https://t.me/cinemazilla">Cɪɴᴇᴍᴀ Zɪʟʟᴀ</a> എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്

നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!</b>

<b>Hɪᴛ /help Tᴏ Kɴᴏᴡ Mʏ ɪɴᴛᴇʀᴇsᴛ Cᴍᴅs Aɴᴅ Fᴇᴀᴛᴜʀᴇs</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔎 𝚈𝚃 𝚂𝙴𝙰𝚁𝙲𝙷", switch_inline_query_current_chat='')
                ],[
                    InlineKeyboardButton("⚠️ 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/cinemazilla"),
                    InlineKeyboardButton("🕵‍♂ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁", url="https://t.me/peaky_blinder_tg"),
                ],[
                    InlineKeyboardButton("💡 𝙷𝙴𝙻𝙿", callback_data="plugins"),
                ],[
                    InlineKeyboardButton("♻️ 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂", callback_data="sourcecode"),
                    InlineKeyboardButton("🔐 𝙲𝙻𝙾𝚂𝙴", callback_data="close"),
                ]
            ]
        ),
    )


@Peaky.on_message(filters.command("help"))
async def help(client, message):
   if message.chat.type == 'private':
       await Peaky.send_message(
               chat_id=message.chat.id,
               text=START_TEXT,
                reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("🏘 𝙷𝙾𝙼𝙴", callback_data="start"),
                InlineKeyboardButton("🔐 𝙲𝙻𝙾𝚂𝙴", callback_data="close"),
            ],[
                InlineKeyboardButton("🤖 𝙰𝙱𝙾𝚄𝚃", url="https://t.me/CINEMAZILLA")
            ]]
           )        
          )

@Peaky.on_callback_query(filters.regex(r"^(start|help|about|close|plugins)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

 if query_data == "plugins":
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

Peaky.run()
