import asyncio
from pyrogram import Client
from info import SESSION, USER_SESSION, API_ID, API_HASH, USER_CHANNELS, BOT_TOKEN
from utils import save_file


async def moin():
    app = Client(USER_SESSION, API_ID, API_HASH)
    await app.start()
    bot = Client(SESSION, API_ID, API_HASH, bot_token=BOT_TOKEN)
    await bot.start()
    for channel in USER_CHANNELS:
        async for user_message in app.iter_history(channel):
            message = await bot.get_messages(
                channel,
                user_message.message_id,
                replies=0
            )
            print(message)
            for file_type in ("document", "video", "audio"):
                media = getattr(message, file_type, None)
                if media is not None:
                    break
            else:
                continue
            media.file_type = file_type
            media.caption = message.caption
            await save_file(media)


asyncio.run(moin())
