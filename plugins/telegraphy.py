#coded by wasim faris 
#follow me on git hub https://GitHub.com/PEAKY-BLINDER-TG
import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("<code>Uploading To Telegraph...</code>")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'<code>Uploaded To Telegraph</code>!\n\n**👉 https://telegra.ph{response[0]}\n\nJoin @cinemazilla**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Client.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("<code>Uploading To Telegraph...</code>")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'<code>Uploaded To Telegraph!</code>\n\n**👉 https://telegra.ph{response[0]}\n\nJoin @cinemazilla**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Client.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @JEBotZ**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Client.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)


link = (
        r"^((?:https?:)?\/\/)"
        r"?((?:www|m)\.)"
       )
       

@Client.on_message(filters.regex(link) & filters.group))
async def(client, message ):
      await message.delete()
