# -*- coding: utf-8 -*-
# -8- pijawca -8-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


rmenu = KeyboardButton(text='📡 Выбрать станцию')
support = KeyboardButton(text='👽 Поддержка')

button1 = InlineKeyboardButton(text='🔘 Europa Plus', url='http://europaplus.hostingradio.ru:8014/europaplus320.mp3')
button2 = InlineKeyboardButton(text='🔘 Comedy Radio', url='https://pub0101.101.ru:8000/stream/air/aac/64/202')
button3 = InlineKeyboardButton(text='🔘 Михаил Круг (Легенда)', url='http://pub0202.101.ru:8000/stream/pro/aac/64/110')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(rmenu).add(support)
kb_choice = InlineKeyboardMarkup().insert(button1).insert(button2).insert(button3)
