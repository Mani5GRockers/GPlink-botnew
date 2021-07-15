from os import environ
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', 'f5d2870b6ae620a908ca908b9889ce308a262ad3')

bot = Client('awslink bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\nWelcome to AWSlink 🎈 {message.chat.first_name}!** \n\nThis is **AWSlink.in | Short URL Bot**. Just send me any big url link for create Short link and share trusted powerful links. \n\n 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗕𝘆 @Mani5GRockers 💖",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('✪ Support Group ✪', url='https://bitly.awslink.in/awsmirrorzone')
                ],
                [
                    InlineKeyboardButton('✪ AWSlink.in ✪', url='https://awslink.in')
                ]
            ]
        )
    )
    
    

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    link = message.matches[0].group(0)
    try:
        short_link = await get_shortlink(link)
        await message.reply(
            text=f"✅ Here is your short link: {short_link}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Open Link 🚀', url=short_link)
                    ]
                ]
            ),
            quote=True
        )
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://bitly.awslink.in/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
