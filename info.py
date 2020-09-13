import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = environ['API_ID']
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Admins & Channels
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(channel) if re.search('^-100\d+$', channel) else channel for channel in environ['CHANNELS'].split()]

# MongoDB information
DATABASE_URI = ['DATABASE_URI']
DATABASE_NAME = ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'