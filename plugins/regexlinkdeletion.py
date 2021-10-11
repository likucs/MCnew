import os 
import pyrogram
from pyrogram import Client, filters


@Client.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me")) | filters.group
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return
