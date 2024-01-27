import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['23328126'])
API_HASH = environ['4958eb0075e7cb4c3cd6d22edc45f974']
BOT_TOKEN = environ['6723793037:AAHyNe4dWe79BQEjcilWgUsMHAGV3UpMJpQ']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['6751187076'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['-1002030879487'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('-1002106601329').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://vishalyadav:vishalyadav@cluster0.xjobpys.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['cluster0']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
Hiii!! 🤩

🍿 Welcome to the world's coolest search engine!

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
