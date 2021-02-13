import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**এই বোটের সাহায্যে আপনি খুব সহজেই পিডিএফ খুঁজতে পারবেন**
নিচের Search Here লিখাতে ক্লিক করে পিডিএফ নাম লিখে খুঁজতে পারবেন বাংলা অথবা ইংরেজী।
আরো জানতে অথবা কিভাবে পিডিএফ খুঁজবেন তা জানতে @pdfsearchhelpbot লিখাতে ক্লিক করুন।
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
