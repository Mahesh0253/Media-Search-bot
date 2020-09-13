from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS
from utils import Media


@Client.on_message(filters.command('start'))
async def start(bot, message):
    """Start command handler"""
    buttons = [[
        InlineKeyboardButton('Search Here', switch_inline_query_current_chat=''),
        InlineKeyboardButton('Go Inline', switch_inline_query=''),
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(START_MSG, reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.chat(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""

    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    for channel in channels:
        channel_info = await bot.get_chat(channel)
        try:
            await message.reply(str(channel_info))
        except Exception as e:
            await message.reply(f'Error: {e}')


@Client.on_message(filters.command('total') & filters.chat(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    total = await Media.count_documents()
    await msg.edit(f'📁 Saved files: {total}')


@Client.on_message(filters.command('logger') & filters.chat(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))