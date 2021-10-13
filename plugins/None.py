from pyrogram import Client as bot
from pyrogram import filters
from wasim_faris.chat_col import present_in_chats, add_to_chats 

@bot.on_message(filters.group, group=2)
async def chats(client, message):
    if not await present_in_chats(message.chat.id):
        await add_to_chats(message.chat.id)
        print("New Group: {message.chat.title}")
