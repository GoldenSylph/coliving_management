#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import os
import asyncio
import aiohttp

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
bot = AsyncTeleBot(os.environ["TELEGRAM_API_KEY"])


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, message.text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

if __name__ == "__main__":
    asyncio.run(bot.polling())
