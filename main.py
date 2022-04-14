#!/usr/bin/python

import os
import asyncio
import aiohttp

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
bot = AsyncTeleBot(os.environ["TELEGRAM_API_KEY"], parse_mode="MARKDOWN")


@bot.message_handler(func=lambda message: True)
async def state_controller(message):
    await bot.reply_to(message, message.text)


if __name__ == "__main__":
    asyncio.run(bot.polling())
