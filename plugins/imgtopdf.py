import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)



LIST = {}

@Client.on_message(filters.command("convertpdf"))
async def pdf(client,message):
 
    if not isinstance(LIST.get(message.from_user.id), list):
      LIST[message.from_user.id] = []

    if not message.reply_to_message:
        return await message.reply("`Reply to a photo to convert it to a pdf..`")

    if not message.reply_to_message.photo:
        return await message.reply("`Reply to a photo to convert it to a pdf..`")
 
    file_id = str(message.reply_to_message.photo.file_id)
    ms = await message.reply_text("<code>Converting to PDF ..</code>")
    file = await client.download_media(file_id)
 
    image = Image.open(file)
    img = image.convert('RGB')
    LIST[message.from_user.id].append(img)
    await ms.edit(f"{len(LIST[message.from_user.id])} image   Successful created PDF if you want add more image Send me One by one\n\n **if done click here 👉 /convert** ")
 

@Client.on_message(filters.command(['convert']))
async def done(client,message):
    images = LIST.get(message.from_user.id)

    if isinstance(images, list):
        del LIST[message.from_user.id]
    if not images:
        return await message.reply_text("No image !!")
     

    path = f"{message.from_user.id}" + ".pdf"
    images[0].save(path, save_all = True, append_images = images[1:])
 
    await client.send_document(message.from_user.id, open(path, "rb"), caption = "Here your pdf !!")
    os.remove(path)
 
