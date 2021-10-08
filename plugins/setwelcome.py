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
