# -*- coding: utf-8 -*-
# -8- pijawca -8-
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram import types
from misc import bot
from handlers.keyboard import kb_client, kb_choice


async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Привет @{message.from_user.username}, используй клавиатуру или команду /menu для выбора радиостанции\n',
        parse_mode=types.ParseMode.MARKDOWN_V2,
        reply_markup=kb_client
    )
    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker=r'CAACAgIAAxkBAAEEIaNiLNeJ-Ma9P1Il0k5-a7vDRpNuaAACQBQAAnsYkEoXOiT9KdXAwCME'
    )

async def support(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'@pijawca',
        parse_mode='HTML'
    )

async def menu(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Выберите радиостанцию',
        reply_markup=kb_choice
    )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start, Text(equals=['/start', '/st']))
    dp.register_message_handler(support, Text(equals=['/support', '👽 Поддержка', '/su']))
    dp.register_message_handler(menu, Text(equals=['/menu', '📡 Выбрать станцию', '/me']))