import os
import requests
from pyrogram import Client as wasim
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


REMOVEBG_API = os.environ.get("REMOVEBG_API", "")
PATH = "./DOWNLOADS/"

ERROR_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

@wasim.on_message(filters.private & (filters.photo | filters.video | filters.document))
async def remove_background(bot, update):
    if not REMOVEBG_API:
        await update.reply_text(
            text="Error :- Remove BG Api is error",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    await update.reply_chat_action("typing")
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    if update and update.media:
        new_file = PATH + str(update.from_user.id) + "/"
        if update.photo or (update.document and "image" in update.document.mime_type):
            new_file_name = new_file + "no_bg.png"
            file = await update.download(PATH+str(update.from_user.id))
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_image = removebg_image(file)
            if new_image.status_code == 200:
                with open(new_file_name, "wb") as image:
                    image.write(new_image.content)
            else:
                await update.reply_text(
                    text="API is error.",
                    quote=True,
                    reply_markup=ERROR_BUTTONS
                )
                return
            await update.reply_chat_action("upload_photo")
            try:
                await update.reply_document(
                    document=new_file_name,
                    quote=True
                )
                await message.delete()
                try:
                    os.remove(file)
                except:
                    pass
            except Exception as error:
                print(error)
                await message.edit_text(
                    text="Something went wrong! May be API limits.",
                    disable_web_page_preview=True,
                    reply_markup=ERROR_BUTTONS
                ) 
    else:
        await message.edit_text(
            text="Media not supported",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )
