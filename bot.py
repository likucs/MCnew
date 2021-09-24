import os
from telegraph import upload_file
import logging
from pyrogram import Client, filters
from config import Config
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

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


START_TEXT ="""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ Cɪɴᴇᴍᴀ Zɪʟʟᴀ  എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്

നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!

👩‍💻 Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ <a href="https://t.me/PEAKY_BLINDER_TG">[★] ᴘᴇᴀᴋʏ вℓιи∂єя [★]</a></b>"""
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
        photo=random.choice(PHOTOS),
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

@Tgraph.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Tgraph.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@Tgraph.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

Peaky.run()
