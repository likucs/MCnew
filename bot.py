import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_TEXT ="""<b>ʜᴇʏ ɪᴀᴍ sɪᴍᴘʟᴇ ʙᴏᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ 

sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴀɴʏ sᴏɴɢ
ᴡɪᴛʜ /song ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɪ ᴡɪʟʟ ᴅᴇғɪɴᴇᴛʟʏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴜʟᴛ ᴡɪᴛʜ ɪɴ sᴇᴄᴏɴᴅs</b>"""
HELP_TEXT = """hey bruhh I can't help you so goway
"""
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

@Peaky.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await update.reply_photo(
        photo="https://telegra.ph/file/fe47bf785fc127335ac1f.jpg",
        caption=f"""**Hello {update.from_user.mention}\nഞാൻ Mᴏᴠɪᴇ Gʀᴀᴍ എന്ന ഗ്രൂപ്പിൽ മൂവി ഫിൽറ്റർ ചെയ്യുന്ന ബോട് അണ്
നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚠️ 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/MGMOVIEGRAM"),
                    InlineKeyboardButton("🕵‍♂ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍", url="https://t.me/Xxxtentacion_TG"),
                ],
                [
                    InlineKeyboardButton("♻️ 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ♻️", url="https://t.me/joinchat/WSO_eDhGmFhmMzE1")
                ],
                [
                    InlineKeyboardButton("💡𝙃𝙀𝙇𝙋", callback_data="about_alert"),
                    InlineKeyboardButton("🔐 𝘾𝙇𝙊𝙎𝙀", callback_data="close"),
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
                InlineKeyboardButton("𝙂𝙊 𝘽𝘼𝘾𝙆", callback_data="start"),
                InlineKeyboardButton("𝘾𝙇𝙊𝙎𝙀", callback_data="close"),
            ],[
                InlineKeyboardButton("GROUP", url="https://t.me/CINEMAZILLA")
            ]]
           )        
          )

# for CallbackQuery
@Peaky.on_callback_query(filters.regex(r"^(start|help|about|close||help_alert)$"), group=2)
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


    if query_data == "help":
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


    if query_data == "about": 
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


    if query_data == "close":
        await update.message.delete()

    if query_data == "help_alert":
        await update.answer("do not type movpie", show_alert=True)
Peaky.run()
