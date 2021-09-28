from pyrogram import Client, filters

@Client.on_message(filters.command(["wasim"]))
async def wasim(bot, message):   
    if message.reply_to_message.photo:
     msg = await bot.send_message(
        text="jdbdvdvvdvfvdvdvdv",
)
    else:
     await msg.edit_text("hrhdvvfbfbfbfbbfbb")
