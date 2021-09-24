import os
import logging
from pyrogram import Client, filters
from config import Config
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_TEXT ="""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ Cɪɴᴇᴍᴀ Zɪʟʟᴀ  എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്

നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!</b>"""
HELP_TEXT = """<b>നീ ഏതാ..... ഒന്ന് പോടെയ് അവൻ help ചോയ്ച്ച് വന്നിരിക്കുന്നു😤...I'm Different Bot U Know</b>"""

CALLBACK_TEXT = """<b>𝙷𝙴𝚈 𝙸𝙰𝙼 𝙹𝚄𝚂𝚃 𝚃𝙴𝚂𝚃 𝙾𝙵 𝙿𝙴𝙰𝙺𝚈 𝙱𝙻𝙸𝙽𝙳𝙴𝚁 </b>"""

ABOUT_TEXT ="""<b>Lɪssᴀ ᴛᴇsᴛ Bᴏᴛ</b>
<b>⍟ DᴇᴠᴇLᴏᴘᴇʀ :- <a href="https://t.me/Xxxtentacion_TG">Xxxtentacion_TG</a></b>
<b>⍟ Credits :- Everyone in this journey</b>
<b>⍟ Server :-<a href="https://herokuapp.com/">Hᴇʀᴏᴋᴜ</a></b>
<b>⍟ source code :- <a href="https://t.me/AdhavaaBiriyaniKittiyalo">Cʟɪᴄᴋ ʜᴇʀᴇ</a></b>
<b>⍟ Library: <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a></b>
<b>~ @no_ones_like_me</b>"""

Peaky = Client(
   "Lisa_bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Peaky.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/fe47bf785fc127335ac1f.jpg",
        caption=f"""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ <a href="https://t.me/cinemazilla">Cɪɴᴇᴍᴀ Zɪʟʟᴀ</a> എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്

നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚠️ 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/cinemazilla"),
                    InlineKeyboardButton("🕵‍♂ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁", url="https://t.me/peaky_blinder_tg"),
                ],
                [
                    InlineKeyboardButton("♻️ 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ♻️", url="https://t.me/cz_films")
                ],
                [
                    InlineKeyboardButton("💡 𝙷𝙴𝙻𝙿", callback_data="help"),
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

# for CallbackQuery

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

Peaky.run()
