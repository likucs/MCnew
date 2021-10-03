import os
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )

@Client.on_message(
    filters.private &
    filters.reply &
    filters.command(["eval", "evaluate", "run"])
)
async def evaluation(bot, update):
    output = evaluate(update.reply_to_message.text)
    try:
        if len(output) < 4096:
            await update.reply_text(
                text=output,
                reply_markup=BUTTONS,
                disable_web_page_preview=True,
                quote=True
            )
        else:
            with BytesIO(str.encode(str(output))) as output_file:
                output_file.name = "output.txt"
                await update.reply_document(
                    document=output_file,
                    caption="Made by @FayasNoushad",
                    reply_markup=BUTTONS,
                    quote=True
                )
    except Exception as error:
        await update.reply_text(
            text=error,
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
