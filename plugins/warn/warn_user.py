import json
import time
from pyrogram import filters
from pyrogram.types import (
    Message,
    ChatPermissions,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from plugins.admin_check import admin_check
from plugins.cust_p_filters import (
    admin_fliter
)

WARN_DATA_ID = int(Config.WARN_DATA_ID)
WARN_SETTINGS_ID = int(Config.WARN_SETTINGS_ID)
COMMAND_HAND_LER = "/"
