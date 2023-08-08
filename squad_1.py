from secret import *
from telebot import types

privet = '''Добро пожаловать, путники!
Здесь, где пути переплетаются и судьбы встречаются,
Откройте двери к неизведанным просторам и вдохновению.
Пусть каждый шаг приносит радость открытия,
И сердце ваше расцветает в объятиях новых миров!'''

privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="1. 1 ответ", callback_data="1 ответ")
privet_markup_btn2 = types.InlineKeyboardButton(
    text="2. 2 ответ", callback_data="2 ответ")
privet_markup_btn3 = types.InlineKeyboardButton(
    text="3. 2 ответ", callback_data="3 ответ")
privet_markup.add(privet_markup_btn1,
                  privet_markup_btn2, privet_markup_btn3)


def send_query(user, answer):
    if answer == "1 отряд":
        states[user] = "1"
        bot.send_message(
            user, privet, reply_markup=privet_markup)
