import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import logging
from pyrogram import Client, filters
import random
import datetime
import json
import string
import traceback
import datetime
import aiofiles
import asyncio
import time
from random import choice 
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from telegraph import upload_file
from database import Database
from config import Config
import asyncio
import os
import time
from info import HU_APP
from pyromod import listen
from asyncio.exceptions import TimeoutError

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
)
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid


API_TEXT = """Hi {}
Welcome to Pyrogram's `HU_STRING_SESSION` generator Bot.
`Send your API_ID to Continue.`"""
HASH_TEXT = "`Send your API_HASH to Continue.`\n\nPress /cancel to Cancel."
PHONE_NUMBER_TEXT = (
    "`Now send your Phone number to Continue"
    " include Country code. eg. +13124562345`\n\n"
    "Press /cancel to Cancel."
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

async def send_msg(user_id, message):
	try:
		await message.copy(chat_id=user_id)
		return 200, None
	except FloodWait as e:
		await asyncio.sleep(e.x)
		return send_msg(user_id, message)
	except InputUserDeactivated:
		return 400, f"{user_id} : deactivated\n"
	except UserIsBlocked:
		return 400, f"{user_id} : user is blocked\n"
	except PeerIdInvalid:
		return 400, f"{user_id} : user id invalid\n"
	except Exception as e:
		return 500, f"{user_id} : {traceback.format_exc()}\n"


BOT_OWNER = int(os.environ["BOT_OWNER"])

DATABASE_URL = os.environ["DATABASE_URL"]

db = Database(DATABASE_URL, "Lissa_test_bot")

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
   plugins=dict(root="plugins")
)

@Peaky.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if not await db.is_user_exist(update.from_user.id):
             await db.add_user(update.from_user.id)
    await update.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""<b>Hᴇʏ {update.from_user.mention}
ഞാൻ <a href="https://t.me/cinemazilla">Cɪɴᴇᴍᴀ Zɪʟʟᴀ</a> എന്ന ഗ്രൂപ്പിൽ  ചുമ്മാ ഇരികുനാ bot അണ്

നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!

𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 <a href="https://t.me/Peaky_blinder_tg">𝚃𝙷𝙸𝚂 𝙱𝙾𝚈𝚈</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Add Me To Your Group ➕", url="t.me/Lissa_test_bot?startgroup=true"),
                ],[
                    InlineKeyboardButton("🕵‍♂ Creator", callback_data="devs"),
                    InlineKeyboardButton("⚠️ Group", url="https://t.me/peaky_blinder_tg"),
                ],[
                    InlineKeyboardButton("💡 Help", callback_data="help"),
                    InlineKeyboardButton("😃 About", callback_data="about"),
                ]
            ]
        ),
    )


@Peaky.on_message(filters.command("help"))
async def help(client, message):
    if not await db.is_user_exist(update.from_user.id):
            await db.add_user(update.from_user.id)
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

@Peaky.on_message(filters.private & filters.command("cast") & filters.user(BOT_OWNER) & filters.reply)
async def broadcast(bot, update):
	broadcast_ids = {}
	all_users = await db.get_all_users()
	broadcast_msg = update.reply_to_message
	while True:
	    broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
	    if not broadcast_ids.get(broadcast_id):
	        break
	out = await update.reply_text(text=f"Broadcast Started! You will be notified with log file when all the users are notified.")
	start_time = time.time()
	total_users = await db.total_users_count()
	done = 0
	failed = 0
	success = 0
	broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
	async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
	    async for user in all_users:
	        sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
	        if msg is not None:
	            await broadcast_log_file.write(msg)
	        if sts == 200:
	            success += 1
	        else:
	            failed += 1
	        if sts == 400:
	            await db.delete_user(user['id'])
	        done += 1
	        if broadcast_ids.get(broadcast_id) is None:
	            break
	        else:
	            broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
	if broadcast_ids.get(broadcast_id):
	    broadcast_ids.pop(broadcast_id)
	completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
	await asyncio.sleep(3)
	await out.delete()
	if failed == 0:
	    await update.reply_text(text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.", quote=True)
	else:
	    await update.reply_document(document='broadcast.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
	os.remove('broadcast.txt')

@Peaky.on_message(filters.private & filters.command("string"))
async def genStr(_, msg: Message):
    chat = msg.chat
    api = await Peaky.ask(
        chat.id, API_TEXT.format(msg.from_user.mention)
    )
    if await is_cancel(msg, api.text):
        return
    try:
        check_api = int(api.text)
    except Exception:
        await msg.reply("`API_ID` is Invalid.\nPress /start to Start again.")
        return
    api_id = api.text
    hash = await Peaky.ask(chat.id, HASH_TEXT)
    if await is_cancel(msg, hash.text):
        return
    if not len(hash.text) >= 30:
        await msg.reply("`API_HASH` is Invalid.\nPress /start to Start again.")
        return
    api_hash = hash.text
    while True:
        number = await Peaky.ask(chat.id, PHONE_NUMBER_TEXT)
        if not number.text:
            continue
        if await is_cancel(msg, number.text):
            return
        phone = number.text
        confirm = await Peaky.ask(chat.id, f'`Is "{phone}" correct? (y/n):` \n\nSend: `y` (If Yes)\nSend: `n` (If No)')
        if await is_cancel(msg, confirm.text):
            return
        if "y" in confirm.text:
            break
    try:
        client = Client("my_account", api_id=api_id, api_hash=api_hash)
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
        return
    try:
        await client.connect()
    except ConnectionError:
        await client.disconnect()
        await client.connect()
    try:
        code = await client.send_code(phone)
        await asyncio.sleep(1)
    except FloodWait as e:
        await msg.reply(f"You have Floodwait of {e.x} Seconds")
        return
    except ApiIdInvalid:
        await msg.reply("API ID and API Hash are Invalid.\n\nPress /start to Start again.")
        return
    except PhoneNumberInvalid:
        await msg.reply("Your Phone Number is Invalid.\n\nPress /start to Start again.")
        return
    try:
        otp = await Peaky.ask(
            chat.id, ("An OTP is sent to your phone number, "
                      "Please enter OTP in `1 2 3 4 5` format. __(Space between each numbers!)__ \n\n"
                      "If Bot not sending OTP then try /restart and Start Task again with /start command to Bot.\n"
                      "Press /cancel to Cancel."), timeout=300)

    except TimeoutError:
        await msg.reply("Time limit reached of 5 min.\nPress /start to Start again.")
        return
    if await is_cancel(msg, otp.text):
        return
    otp_code = otp.text
    try:
        await client.sign_in(phone, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
    except PhoneCodeInvalid:
        await msg.reply("Invalid Code.\n\nPress /start to Start again.")
        return
    except PhoneCodeExpired:
        await msg.reply("Code is Expired.\n\nPress /start to Start again.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await Peaky.ask(
                chat.id, 
                "Your account have Two-Step Verification.\nPlease enter your Password.\n\nPress /cancel to Cancel.",
                timeout=300
            )
        except TimeoutError:
            await msg.reply("`Time limit reached of 5 min.\n\nPress /start to Start again.`")
            return
        if await is_cancel(msg, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await client.check_password(new_code)
        except Exception as e:
            await msg.reply(f"**ERROR:** `{str(e)}`")
            return
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`")
        return
    try:
        session_string = await client.export_session_string()
        await client.send_message("me", f"#PYROGRAM #STRING_SESSION\n\n```{session_string}```")
        await client.disconnect()
        text = "String Session is Successfully Generated.\nClick on Below Button."
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Show String Session", url=f"tg://openmessage?user_id={chat.id}")]]
        )
        await Peaky.send_message(chat.id, text, reply_markup=reply_markup)
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`")
        return


@Peaky.on_message(filters.private & filters.command("restart"))
async def restart(_, msg: Message):
    await msg.reply("Restarted Bot!")
    HU_APP.restart()


async def is_cancel(msg: Message, text: str):
    if text.startswith("/cancel"):
        await msg.reply("Process Cancelled.")
        return True
    return False

@Peaky.on_message((filters.private | filters.group) & filters.command('status'))
async def bot_status(client,message):
    if str(message.from_user.id) not in Config.AUTH_USERS:
        return

    chats, filters = await filter_stats()

    if Config.SAVE_USER == "yes":
        users = await all_users()
        userstats = f"> __**{users} users have interacted with your bot!**__\n\n"
    else:
        userstats = ""

    if Config.HEROKU_API_KEY:
        try:
            server = heroku3.from_key(Config.HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {Config.HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

                quota_details = f"""

**Heroku Account Status**

> __You have **{total} hours** of free dyno quota available each month.__

> __Dyno hours used this month__ ;
        - **{used} hours**  ( {usedperc}% )

> __Dyno hours remaining this month__ ;
        - **{hours} hours**  ( {leftperc}% )
        - **Approximately {days} days!**


"""
            else:
                quota_details = ""
        except:
            print("Check your Heroku API key")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - Config.BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**Disk Details**\n\n" \
            f"> USED  :  {used} / {total}\n" \
            f"> FREE  :  {free}\n\n"
    except:
        disk = ""

    await message.reply_text(
        "**Current status of your bot!**\n\n"
        f"> __**{filters}** filters across **{chats}** chats__\n\n"
        f"{userstats}"
        f"> __BOT Uptime__ : **{uptime}**\n\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode="md"
    )


x = datetime.datetime.now()
print(x)
Peaky.run()
