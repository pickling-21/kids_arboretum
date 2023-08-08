from telebot import types
from secret import *

privet = "Привет, путник. Нам нужна твоя помощь. Отправляйся к большой красной рыбе, которая думает что она чайка, она все расскажет. И помни, что времени мало. Удачи."


privet_markup = types.InlineKeyboardMarkup()  # создаем клавиатуру
privet_markup_btn1 = types.InlineKeyboardButton(
    text="Миссию принял", callback_data="операция рад")
# создаем кнопку
privet_markup.add(privet_markup_btn1)
# добавить кнопку на клавиатуру

basket = 'Иди к баскетбольному кольцу'
basket_markup = types.InlineKeyboardMarkup()
basket_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, пойду", callback_data="пошел к кольцу")
basket_markup.add(basket_markup_btn1)


def send_query(user, answer):
    if answer == "4 отряд":
        states[user] = "4"
        bot.send_message(
            user, privet, reply_markup=privet_markup)

    if answer == 'операция рад':
        bot.send_message(user, basket, reply_markup=basket_markup)
