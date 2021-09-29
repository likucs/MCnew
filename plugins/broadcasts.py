
import os
import logging
from pyrogram import Client, filters
from pyrogram import StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Config import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, TUTORIAL, BROADCAST_CHANNEL, DB_URL, SESSION, ADMIN_ID    
from LuciferMoringstar_Robot.Utils import Media, get_file_details 
from LuciferMoringstar_Robot.Broadcast import broadcast
from LuciferMoringstar_Robot import ABOUT
from LuciferMoringstar_Robot.Channel import handle_user_status
from Database import Database
from pyrogram.errors import UserNotParticipant

@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in ADMIN_ID:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)
