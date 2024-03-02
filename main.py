from squads import markups as m
from squads import squad_1 as a
from squads import squad_2 as b
from squads import squad_3 as c
from squads import squad_4 as d
from squads import squad_5 as e
from squads import squad_6 as f

from squads.data import *
from telebot import TeleBot, types
from random import randint


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
    a.send_text(user, text)
    f.send_text(user, text)
    if c.send_text(user, text) == False and curr_squad == 3:
        bot.send_message(user, 'не то')
    if d.send_text(user, text) == False and curr_squad == 4:
        bot.send_message(user, 'не то')
    if e.send_text(user, text) == False and curr_squad == 5:
        bot.send_message(user, 'не то')

    # отправляем сообщение тому же пользователю с тем же текстом


@bot.message_handler(content_types=['video_note', 'video'])
def send_video(message):
    user = message.chat.id
    # отправляем сообщение тому же пользователю с тем же текстом
    if states[user] == '3 белка':
        bot.send_message(user, c.thanks, reply_markup=c.thanks_markup)
        states[user] = "1 видио есть"
    e.send_video(user)
    b.send_video(user)


@bot.message_handler(content_types=['photo'])
def send_video(message):
    user = message.chat.id
    e.send_photo(user)
    d.send_photo(user)


@bot.message_handler(content_types=['voice'])
def send_voice(message):
    user = message.chat.id
    # отправляем сообщение тому же пользователю с тем же текстом
    if states[user] == 'ждем веер':
        bot.send_message(user, c.veer)
        states[user] = "веер"

    e.send_voice(user)


@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    answer = call.data

    if answer == 'вернуться':
        answer = 'начало'

    if answer == 'правила':
        bot.send_message(user, m.pravila, parse_mode='Markdown',
                         reply_markup=m.pravila_markup)

    if answer == "начало":
        bot.send_photo(user, m.karta)
        bot.send_message(user, m.poryadok)
        bot.send_message(
            user, 'Куда пойдем?', reply_markup=m.begin_markup)

    a.send_query(user, answer)
    b.send_query(user, answer)
    c.send_query(user, answer)
    d.send_query(user, answer)
    e.send_query(user, answer)
    f.send_query(user, answer)



if __name__ == "__main__":
    
    bot.polling(non_stop=True)