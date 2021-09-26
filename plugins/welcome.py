# Thanks bug hunter for repo
# scraped from bughunter
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid=message.chat.id
	await bot.send_photo(
        chatid=message.chat.id
        photo="https://telegra.ph/file/83dd03f6cd75ffb341a9e.jpg",
        caption=f"Welcome {message.from_user.mention} to {message.chat.username} ,  Happy to have here",chat_id=chatid)
       
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	
