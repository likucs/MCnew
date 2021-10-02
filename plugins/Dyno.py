
import os
import math
import json
import time
import shutil
import heroku3
import requests

from pyrogram import filters
from pyrogram import Client as trojanz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

if bool(os.environ.get("WEBHOOK", False)):
from config import Config

from plugins.helpers import humanbytes
from wasim_faris.filter_db import filter_stats
from wasim_faris.users_mdb import add_user, find_user, all_users
