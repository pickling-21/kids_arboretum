from secret import *
from telebot import types

privet = '''Это 6 отряд'''

privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="6 район рулит!!!", callback_data="монстры")
privet_markup.add(privet_markup_btn1)


def send_query(user, answer):
    if answer == "6 отряд":
        states[user] = "6"
        bot.send_message(
            user, privet, reply_markup=privet_markup)
