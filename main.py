import markups as m
import squad_1 as a
import squad_2 as b
import squad_3 as c
import squad_4 as d
import squad_5 as e
import squad_6 as f

from secret import *
from telebot import TeleBot, types
from random import randint

# словарь картинок для квеста


@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.chat.id
    states[user] = "0"
    bot.send_message(
        user, 'Привет, сегодня тебе предстоит пройти квест по лагерю "Чайка"! Готов начать?', reply_markup=m.start_markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    text = message.text
    user = message.chat.id
    c.send_text(user, text)
    # отправляем сообщение тому же пользователю с тем же текстом


@bot.message_handler(content_types=['video_note'])
def send_video(message):
    user = message.chat.id
    # отправляем сообщение тому же пользователю с тем же текстом
    if states[user] == '3 белка':
        bot.send_message(user, c.thanks, reply_markup=c.thanks_markup)
        states[user] = "1 видио есть"


@bot.message_handler(content_types=['voice'])
def send_video(message):
    user = message.chat.id
    # отправляем сообщение тому же пользователю с тем же текстом
    if states[user] == 'ждем веер':
        bot.send_message(user, c.veer)
        states[user] = "веер"


@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    answer = call.data

    if answer == 'вернуться':
        states[user] = "0"

    if answer == "начало":
        bot.send_message(
            user, 'Куда пойдем?', reply_markup=m.begin_markup)

    a.send_query(user, answer)
    b.send_query(user, answer)
    c.send_query(user, answer)
    d.send_query(user, answer)
    e.send_query(user, answer)
    f.send_query(user, answer)


bot.polling(non_stop=True)
