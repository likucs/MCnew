import re
from os import environ
from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_HASH = environ['API_HASH']


COMMAND_HAND_LER = "/"

HU_APP = from_key(API_KEY).apps()[APP_NAME]

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

# Messages

default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = """
%┈••✿ @MGMOVIEGRAM ✿••┈
➠𝐂ʜᴀɴɴᴇʟ : https://t.me/joinchat/WSO_eDhGmFhmMzE1
➠Gʀᴏᴜᴘ : https://t.me/joinchat/0jh0z1b3OgQ2MGI1</b>**
"""


OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
