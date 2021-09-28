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

HELP_TEXT = """<b>നീ ഏതാ..... ഒന്ന് പോടെയ് അവൻ help ചോയ്ച്ച് വന്നിരിക്കുന്നു😤...I'm Different Bot U Know</b>"""

CALLBACK_TEXT = """<b>𝙷𝙴𝚈 𝙸𝙰𝙼 𝙹𝚄𝚂𝚃 𝚃𝙴𝚂𝚃 𝙾𝙵 𝙿𝙴𝙰𝙺𝚈 𝙱𝙻𝙸𝙽𝙳𝙴𝚁 </b>"""

ABOUT_TEXT ="""<b>★ 𝙼𝚈 𝙽𝙰𝙼𝙴 :- 𝙻𝙸𝚂𝚂𝙰 𝙱𝙾𝚃</b>
<b>★ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 :- <a href="https://t.me/Xxxtentacion_TG">𝚇𝚇𝚇𝚃𝙴𝙽𝚃𝙰𝙲𝚃𝙸𝙾𝙽_𝚃𝙶</a></b>
<b>★ 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 :- 𝙴𝚅𝙴𝚁𝚈 𝙾𝙽𝙴 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙹𝙾𝚄𝚁𝙽𝙴𝚈</b>
<b>★ 𝚂𝙴𝚁𝚅𝙴𝚁 :- <a href="https://herokuapp.com/">𝙷𝙴𝚁𝙾𝙺𝚄</a></b>
<b>★ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 :- <a href="https://t.me/AdhavaaBiriyaniKittiyalo">𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a></b>
<b>★ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 :- <a href="https://github.com/pyrogram/pyrogram">𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a></b>"""


Peaky = Client(
   "Lisa_bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
   plugins=dict(root="plugins, lissa")
)

@Peaky.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    await update.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ <a href="https://t.me/cinemazilla">Cɪɴᴇᴍᴀ Zɪʟʟᴀ</a> എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്

നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!

𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 <a href="https://t.me/Peaky_blinder_tg">𝚃𝙷𝙸𝚂 𝙱𝙾𝚈𝚈</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔎  𝚈𝚃 𝚂𝙴𝙰𝚁𝙲𝙷", switch_inline_query_current_chat='')
                ],[
                    InlineKeyboardButton("🕵‍♂ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁", callback_data="devs"),
                    InlineKeyboardButton("⚠️ 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/peaky_blinder_tg"),
                ],[
                    InlineKeyboardButton("💡 𝙷𝙴𝙻𝙿", callback_data="help"),
                    InlineKeyboardButton("♻️ 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂", callback_data="home"),
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
Peaky.run()
