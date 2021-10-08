import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.new_chat_members)
async def auto_welcome(bot: Client, msg: Message):
    # from PR0FESS0R-99 import ID-Bot
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    welcome_text = f"👋Hey {mention}, Welcome To {group_name}\n\n Developed By @Mo_Tech_YT"
    welcome_msg = os.environ.get(f"WELCOME_TEXT", welcome_text)
    print("Welcome Message Activate")
    await msg.reply_text(text=welcome_msg.format(
        first = msg.from_user.first_name,
        last = msg.from_user.last_name,
        username = None if not msg.from_user.username else '@' + msg.from_user.username,
        mention = msg.from_user.mention,
        id = msg.from_user.id,
        group_name = msg.chat.title,
        group_username = None if not msg.chat.username else '@' + msg.chat.username
   )

@Client.on_message(filters.private & filters.command("admin"))
async def admin(bot: Client, update):
    # Heroku Support
    user_admin = "Open Heroku => Application => Settings => Config Vars => Welcome_Text Edit"
    user = "👋Hey {}, \n You are not the deploy of this bot"
    run = "PR0FESS0R-99/Auto-Welcome-Bot" # https://github.com/PR0FESS0R-99/Auto-Welcome-Bot
    api_key = os.environ.get("APP_NAME", "")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split()) 
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "⚙️HEROKU SETTINGS⚙️", url=f"https://dashboard.heroku.com/apps/{api_key}/settings"
                    )
            ]
        ]
    )
    deploy =InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "💫 DEPLOY NOW 💫", url=f"https://heroku.com/deploy?template=https://github.com/{run}/tree/main"
                    )
            ]
        ]
    )
    if update.from_user.id not in OWNER_ID:
        await update.reply_text(text=user.format(update.from_user.mention), reply_markup=deploy)
        return
    await update.reply_text(text=user_admin, reply_markup=reply_markup)
   
