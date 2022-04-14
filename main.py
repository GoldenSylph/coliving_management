#!/usr/bin/python

import os
import asyncio
import aiohttp

from enum import Enum
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from telebot import types

load_dotenv()
bot = AsyncTeleBot(os.environ["TELEGRAM_API_KEY"], parse_mode="MARKDOWN")

class State(Enum):
    START = 0
    DEBTS = 1
    INFO = 2

current_state = State.START

@bot.message_handler(commands=['start'])
async def start_controller(message):
    current_state = State.START
    markup = types.ReplyKeyboardMarkup(row_width=2)
    debts_button = types.KeyboardButton('Debts')
    info_button = types.KeyboardButton('Info')
    markup.add(debts_button, info_button)
    await bot.reply_to(message, 'Hi! Choose the mode:', reply_markup=markup)


@bot.message_handler(func: lambda message: True)
async def state_controller(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    if current_state == State.START:
        if message.text == "Debts":
            current_state = State.DEBTS
            await bot.reply_to(message, )
            
        elif message.text == "Info":
            current_state = State.INFO
            await bot.reply_to(message, 'Just jab something...')
        else:
            await bot.reply_to(message, 'Please use the buttons or type "/start".')
    elif current_state == State.DEBTS:
        add_me_button = types.KeyboardButton('Add me to the list')
        record_debt_button = types.KeyboardButton('Record debt')
        markup.add(add_me_button, record_debt_button)
        await bot.reply_to(message, 'Ok, let\'s start with debts management:', reply_markup=markup)
    elif current_state == State.INFO:
        await bot.reply_to(message, 'This is a small coliving management bot for our friends. Made by Oleg and Dima.')
        current_state = State.START
    else:
        await bot.reply_to(message, 'AN UNKNOWN STATE, PLEASE ADDRESS THE ADMINISTRATION')


if __name__ == "__main__":
    asyncio.run(bot.polling())
