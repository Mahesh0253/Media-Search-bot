from pyrogram import Client, filters
from utils import save_file
from info import CHANNELS

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for kind in ("document", "video", "audio"):
        media = getattr(message, kind, None)
        if media is not None:
            break
    else:
        return
    
    media.file_type = kind
    media.caption = message.caption
    await save_file(media)