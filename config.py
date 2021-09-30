import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

    ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())

    
