import re
from os import environ
from heroku3 import from_key
from pyrogram import Client
from config import Config
from pyromod import listen
import re
import time

from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
import re
from typing import List

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_HASH = environ['API_HASH']


COMMAND_HAND_LER = "/"

HEROKU_API_KEY = "77961583-b642-42a7-b31f-e4eea6880508"

HU_APP = "nthingdnbdbd"
SAVE_USER = "yes"

TG_MAX_SELECT_LEN = "1000"
DB_URI = Config.DB_URI
BOT_START_TIME = time.time()
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users

ADMINS = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]

AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information

FILTER_DB_URI = "mongodb+srv://wasim:wasim@cluster0.wc1o6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# auth groups

AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

SUDO_USERS = "1287385877"




USE_AS_BOT = True

