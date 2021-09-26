# Thanks bug hunter for repo
# scraped from bughunter
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
  buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)

	chatid=message.chat.id
	await bot.send_message(text=f"Welcome {message.from_user.mention} to {message.chat.username} ,  Happy to have here",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Bye ,  {message.from_user.mention} , Have a Nice Day",chat_id=chatid)
	
