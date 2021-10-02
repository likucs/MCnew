import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

    ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())

    FILTER_DB_URI = "mongodb+srv://wasim:wasim@cluster0.wc1o6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    WARN_DATA_ID = "1"

    WARN_SETTINGS_ID = "56"

    DB_URI = os.environ.get("DATABASE_URL", None)

    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())


    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
