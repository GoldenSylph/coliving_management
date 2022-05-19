#!/usr/bin/python

import os
import asyncio

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from telebot import types

from forms.base import Context
from forms.states import AddPaymentDateState

load_dotenv()
bot = AsyncTeleBot(os.environ["TELEGRAM_API_KEY"], parse_mode="MARKDOWN")
context = Context()

@bot.message_handler(commands=['start', 'help'])
async def start_controller(message):
    context.set_state(None)
    markup = types.ReplyKeyboardMarkup(row_width=2)
    debts_button = types.KeyboardButton('/add_debt')
    info_button = types.KeyboardButton('/info')
    markup.add(debts_button, info_button)
    await bot.reply_to(message, 'Hi! Choose the mode:', reply_markup=markup)


@bot.message_handler(commands=['add_debt'])
async def debts_controller(message):
    if context.current_state == None:
        context.set_state(AddPaymentDateState())
    markup = types.ReplyKeyboardRemove(selective=False)
    await bot.reply_to(message, "We are starting the Adding Debt Form", reply_markup=markup)
    await context.action(bot, message)


@bot.message_handler(func=lambda m: True)
async def context_controller(message):
    if context.current_state == None:
        await bot.reply_to(message, "Please use the buttons or type valid command.")
    else:
        await context.action(bot, message)


@bot.message_handler(commands=['info'])
async def info_controller(message):
    await bot.reply_to(message, 'The authors are: Dmitry Zanadvornych, Oleg Bedrin')


if __name__ == "__main__":
    asyncio.run(bot.polling())
