
from telebot import TeleBot, types
from random import randint
# токен для бота
from secret import token

import markups as m
# словарь картинок для квеста

pictures = {
    0: "https://kmv-tur.org/sites/default/files/node/camp/field_images3/2021-05/be6cf54956661e553242225d536ada4a.jpg",
    1: "https://img.tourister.ru/files/2/1/0/7/2/7/6/1/original.jpg",
    2: "https://img.ixbt.site/live/topics/preview/00/03/75/54/74b9058c4c.jpg",
    3: "https://mylnaya-opera.ru/481-large_default/zagotovka-dlya-dekupazha-nadpis-informaciya.jpg",
    4: "https://mylnaya-opera.ru/481-large_default/zagotovka-dlya-dekupazha-nadpis-informaciya.jpg"}

bot = TeleBot(token)

states = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.chat.id
    states[user] = "0"
    bot.send_message(
        user, 'Привет, сегодня тебе предстоит пройти квест по лагерю "Чайка"! Готов начать?', reply_markup=m.start_markup)


@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    answer = call.data

    if answer == 'вернуться':
        states[user] = "0"

    if states[user] == "0":
        bot.send_message(
            user, 'Куда пойдешь?', reply_markup=m.begin_markup)
        states[user] = "пошел"

    if answer == "1 отряд":
        states[user] = "9"
        bot.send_message(
            user, 'Выбери', reply_markup=m.first_squad_markup)

    if answer == "дендропарк":
        states[user] = "9"
        bot.send_message(
            user, 'Выбери', reply_markup=m.first_squad_markup)

    if answer == "1 ответ":
        states[user] = "9"
        bot.send_message(
            user, 'правильно', reply_markup=m.back_first_markup)

    if answer == "2 ответ":
        states[user] = "9"
        bot.send_message(
            user, 'неправильно', reply_markup=m.back_first_markup)


bot.polling(non_stop=True)
