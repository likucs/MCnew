import os
import re
import io
import pyrogram
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import ADMINS

from wasim_faris.filter_db import add_filter
from wasim_faris.filter_db import find_filter
from wasim_faris.filter_db import get_filters
from wasim_faris.filter_db import delete_filter
from wasim_faris.filter_db import count_filters

from wasim_faris.connect_db import add_connection
from wasim_faris.connect_db import all_connections
from wasim_faris.connect_db import if_active
from wasim_faris.connect_db import delete_connection
from wasim_faris.connect_db import active_connection
from plugins.main_filter.Helpers import parser,split_quotes


@Client.on_message(filters.private & filters.command(["connections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "There are no active connections!! Connect to some groups first.",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            if active:
                act = " - ACTIVE"
            else:
                act = ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{title}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "Your connected group details ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
