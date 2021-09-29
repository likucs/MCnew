import os
import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")
    
    WARN_DATA_ID = int(os.environ.get("WARN_DATA_ID", "0"))
    WARN_SETTINGS_ID = int(os.environ.get("WARN_SETTINGS_ID", "0"))
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    USE_AS_BOT = int(os.environ.get("USE_AS_BOT", "0"))
