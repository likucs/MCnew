import os
from telegraph import upload_file
import logging
from pyrogram import Client, filters
from config import Config
import random
from pyrogram import Client, filters
import math
import json
import shutil
from requests.utils import requote_uri

import youtube_dl
from youtube_search import YoutubeSearch
import requests

from pyrogram import Client, errors
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from youtubesearchpython import VideosSearch

import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio

from asyncio.exceptions import TimeoutError

from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired
)

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

@Peaky.on_message(filters.photo)
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

@Peaky.on_message(filters.animation)
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

@Peaky.on_message(filters.video)
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

@Peaky.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('`Fetching....from..my..database... Please Wait...`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 7000:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[eva/🇮🇳]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**NO DATA FOUNDED WITH THIS TRY WITH ANOTHER !**')
            return
    except Exception as e:
        m.edit(
            "**Enter Song Name with /song Command!**"
        )
        print(str(e))
        return
    m.edit("`... Uploading... PLEASE.....BE..PATIENT...`")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 <b>Title:</b> <a href="{link}">{title}</a>\n⌚ <b>Duration:</b> <code>{duration}</code>\n📻 <b>Uploaded By:</b> <a href="https://t.me/EVA_V3_BOT">🎧 eva 🎧</a>'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('**AN ERROR OCCURED REPORT THIS AT @NAZRIYASUPPORT!!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@Peaky.on_message(filters.command('info') & (filters.private | filters.group))
async def showinfo(client, message):
    try:
        cmd, id = message.text.split(" ", 1)
    except:
        id = False
        pass

    if id:
        if (len(id) == 10 or len(id) == 9):
            try:
                checkid = int(id)
            except:
                await message.reply_text("__Enter a valid USER ID__", quote=True, parse_mode="md")
                return
        else:
            await message.reply_text("__Enter a valid USER ID__", quote=True, parse_mode="md")
            return           

        if Config.SAVE_USER == "yes":
            name, username, dcid = await find_user(str(id))
        else:
            try:
                user = await client.get_users(int(id))
                name = str(user.first_name + (user.last_name or ""))
                username = user.username
                dcid = user.dc_id
            except:
                name = False
                pass

        if not name:
            await message.reply_text("__USER Details not found!!__", quote=True, parse_mode="md")
            return
    else:
        if message.reply_to_message:
            name = str(message.reply_to_message.from_user.first_name\
                    + (message.reply_to_message.from_user.last_name or ""))
            id = message.reply_to_message.from_user.id
            username = message.reply_to_message.from_user.username
            dcid = message.reply_to_message.from_user.dc_id
        else:
            name = str(message.from_user.first_name\
                    + (message.from_user.last_name or ""))
            id = message.from_user.id
            username = message.from_user.username
            dcid = message.from_user.dc_id
    
    if not str(username) == "None":
        user_name = f"@{username}"
    else:
        user_name = "none"

    await message.reply_text(
        f"<b>Name</b> : {name}\n\n"
        f"<b>User ID</b> : <code>{id}</code>\n\n"
        f"<b>Username</b> : {user_name}\n\n"
        f"<b>Permanant USER link</b> : <a href='tg://user?id={id}'>Click here!</a>\n\n"
        f"<b>DC ID</b> : {dcid}\n\n",
        quote=True,
        parse_mode="html"
    )


API_TEXT = """🙋‍♂ Hi {},
**I am a String Session generator bot.**
**For generating string session send me your** `API_ID` 🐿
**👇Tutorial Video👇**
👉**ʜᴏᴡ ᴛᴏ ɢᴇᴛ ᴀᴘɪ ɪᴅ & ᴀᴘɪ ʜᴀsʜ** <a href='https://youtu.be/5eEsvLAKVc0'>Video Link</a>
👉**ʜᴏᴡ ᴛᴏ ɢᴇᴛ ᴜsᴇʀsᴇssɪᴏɴ ꜰᴏʀ ᴡᴇʙsɪᴛᴇ** <a href='https://youtu.be/WUN_12-dYOM'>Video Link</a>
**👤Any Doubt @Mo_Tech_Group**
**🤔Any Help**  /help
**🤖About Bot** /about
"""

HASH_TEXT = "Ok Now Send your `API_HASH` to Continue.\n\nPress /cancel to Cancel.🐧"
PHONE_NUMBER_TEXT = (
    "📞__ Now send your Phone number to Continue"
    " include Country code.__\n**Eg:** `+13124562345`\n\n"
    "Press /cancel to Cancel."
)



@Peaky.on_message(filters.private & filters.command("string"))
async def generate_str(c, m):
    get_api_id = await c.ask(
        chat_id=m.chat.id,
        text=API_TEXT.format(m.from_user.mention(style='md')),
        filters=filters.text
    )
    api_id = get_api_id.text
    if await is_cancel(m, api_id):
        return

    await get_api_id.delete()
    await get_api_id.request.delete()
    try:
        check_api = int(api_id)
    except Exception:
        await m.reply("**--🛑 API ID Invalid 🛑--**\nPress /start to create again.")
        return

    get_api_hash = await c.ask(
        chat_id=m.chat.id, 
        text=HASH_TEXT,
        filters=filters.text
    )
    api_hash = get_api_hash.text
    if await is_cancel(m, api_hash):
        return

    await get_api_hash.delete()
    await get_api_hash.request.delete()

    if not len(api_hash) >= 30:
        await m.reply("--**🛑 API HASH Invalid 🛑**--\nPress /start to create again.")
        return

    try:
        client = Client("my_account", api_id=api_id, api_hash=api_hash)
    except Exception as e:
        await c.send_message(m.chat.id ,f"**🛑 ERROR: 🛑** `{str(e)}`\nPress /start to create again.")
        return

    try:
        await client.connect()
    except ConnectionError:
        await client.disconnect()
        await client.connect()
    while True:
        get_phone_number = await c.ask(
            chat_id=m.chat.id,
            text=PHONE_NUMBER_TEXT
        )
        phone_number = get_phone_number.text
        if await is_cancel(m, phone_number):
            return
        await get_phone_number.delete()
        await get_phone_number.request.delete()

        confirm = await c.ask(
            chat_id=m.chat.id,
            text=f'🤔 Is `{phone_number}` correct? (y/n): \n\ntype: `y` (If Yes)\ntype: `n` (If No)'
        )
        if await is_cancel(m, confirm.text):
            return
        if "y" in confirm.text.lower():
            await confirm.delete()
            await confirm.request.delete()
            break
    try:
        code = await client.send_code(phone_number)
        await asyncio.sleep(1)
    except FloodWait as e:
        await m.reply(f"__Sorry to say you that you have floodwait of {e.x} Seconds 😞__")
        return
    except ApiIdInvalid:
        await m.reply("🕵‍♂ The API ID or API HASH is Invalid.\n\nPress /start to create again.")
        return
    except PhoneNumberInvalid:
        await m.reply("☎ Your Phone Number is Invalid.`\n\nPress /start to create again.")
        return

    try:
        sent_type = {"app": "Telegram App 💌",
            "sms": "SMS 💬",
            "call": "Phone call 📱",
            "flash_call": "phone flash call 📲"
        }[code.type]
        otp = await c.ask(
            chat_id=m.chat.id,
            text=(f"I had sent an OTP to the number `{phone_number}` through {sent_type}\n\n"
                  "Please enter the OTP in the format `1 2 3 4 5` __(provied white space between numbers)__\n\n"
                  "If Bot not sending OTP then try /start the Bot.\n"
                  "Press /cancel to Cancel."), timeout=300)
    except TimeoutError:
        await m.reply("**⏰ TimeOut Error:** You reached Time limit of 5 min.\nPress /start to create again.")
        return
    if await is_cancel(m, otp.text):
        return
    otp_code = otp.text
    await otp.delete()
    await otp.request.delete()
    try:
        await client.sign_in(phone_number, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
    except PhoneCodeInvalid:
        await m.reply("**📵 Invalid Code**\n\nPress /start to create again.")
        return 
    except PhoneCodeExpired:
        await m.reply("**⌚ Code is Expired**\n\nPress /start to create again.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await c.ask(
                chat_id=m.chat.id, 
                text="`🔐 This account have two-step verification code.\nPlease enter your second factor authentication code.`\nPress /cancel to Cancel.",
                timeout=300
            )
        except TimeoutError:
            await m.reply("**⏰ TimeOut Error:** You reached Time limit of 5 min.\nPress /start to create again.")
            return
        if await is_cancel(m, two_step_code.text):
            return
        new_code = two_step_code.text
        await two_step_code.delete()
        await two_step_code.request.delete()
        try:
            await client.check_password(new_code)
        except Exception as e:
            await m.reply(f"**⚠️ ERROR:** `{str(e)}`")
            return
    except Exception as e:
        await c.send_message(m.chat.id ,f"**⚠️ ERROR:** `{str(e)}`")
        return
    try:
        session_string = await client.export_session_string()
        await client.send_message("me", f"**Your String Session 👇**\n\n`{session_string}`\n\nThanks For using {(await c.get_me()).mention(style='md')}")
        text = "✅ Successfully Generated Your String Session and sent to you saved messages.\nCheck your saved messages or Click on Below Button."
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="String Session ↗️", url=f"tg://openmessage?user_id={m.chat.id}")]]
        )
        await c.send_message(m.chat.id, text, reply_markup=reply_markup)
    except Exception as e:
        await c.send_message(m.chat.id ,f"**⚠️ ERROR:** `{str(e)}`")
        return

Peaky.run()
