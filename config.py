import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

    ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())

    FILTER_DB_URI = "mongodb+srv://wasim:wasim@cluster0.wc1o6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
 
    ADMINS = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]


    auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
  
    AUTH_USERS = (auth_users + ADMINS) if auth_users else []


    
