import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *

API = "https://apibu.herokuapp.com/api/y-images?query="

@Client.on_inline_query()
async def search(bot, update):
    requests.get(API + requote_uri(update.query)).json()["result"][:50]
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query,
                description=result,
                caption="Made by @FayasNoushad",
                photo_url=result
            )
        )
    await update.answer(answers)
