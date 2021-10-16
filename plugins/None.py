from pyrogram import Client as bot
from pyrogram import filters

@bot.on_message(filters.group, group=2)
async def chats(client, message):
    if not await present_in_chats(message.chat.id):
        await add_to_chats(message.chat.id)
        print("New Group: {message.chat.title}")
