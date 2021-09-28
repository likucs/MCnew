from pyrogram import Client, filters

@Client.on_message(filters.command(["wasim"]))
async def wasim(bot, message):   
    if message.reply_to_message.sticker:
     msg = await bot.send_text("jdbdvdvvdvfvdvdvdv")
    else:
     await msg.edit_text("hrhdvvfbfbfbfbbfbb")
