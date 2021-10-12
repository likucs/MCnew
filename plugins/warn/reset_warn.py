import json
from pyrogram import Client, filters
from pyrogram.types import (
    Message
)

from plugins.cust_p_filters import (
    admin_fliter
)
from config import Config
WARN_DATA_ID = int(Config.WARN_DATA_ID)
WARN_SETTINGS_ID = int(Config.WARN_SETTINGS_ID)
COMMAND_HAND_LER = "/"


@Client.on_message(
    filters.command(["resetwarn"], COMMAND_HAND_LER) &
    admin_fliter
)
async def reset_all_warns(client: Client, msg: Message):
    replied = msg.reply_to_message
    if not replied:
        return
    user_id = str(replied.from_user.id)
    if replied.from_user.is_self:
        return
    chat_id = str(msg.chat.id)
    if chat_id not in client.warndatastore:
        client.warndatastore[chat_id] = {}
    DATA = client.warndatastore[chat_id]
    if DATA.get(user_id):
        DATA.pop(user_id)
        await msg.reply("All Warns are removed for this User.")
    else:
        await msg.reply("User already not have any warn.")
    client.warndatastore[chat_id] = DATA
    await client.save_public_store(
        WARN_DATA_ID,
        json.dumps(client.warndatastore)
    )