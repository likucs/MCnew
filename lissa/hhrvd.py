from pyrogram import Client, filters

# Sticker ID 
@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
    await message.replay("heyibfbfbbfbfbbf",)
  else :
    await message.replay("jdhhdhfbfbdndnfb",)
