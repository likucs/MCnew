import os 
import pyrogram
from pyrogram import Client, filters


@Client.on_message(filters.regex("t.me"))
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return
