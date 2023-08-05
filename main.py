
import markups as m
import squad_1 as a
import squad_2 as b
import squad_3 as c
import squad_4 as d
import squad_5 as e
import squad_6 as f


from telebot import TeleBot, types
from random import randint

# токен для бота
token = "6365845419:AAGzeRqMSyEFhoGQwJ4pdFd5f-R0kvGjtSI"


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
        states[user] = "1"
        bot.send_message(
            user, a.privet, reply_markup=a.privet_markup)

    if answer == "2 отряд":
        states[user] = "2"
        bot.send_message(
            user, b.privet, reply_markup=b.privet_markup)

    if answer == "3 отряд":
        states[user] = "3"
        bot.send_message(
            user, c.privet, reply_markup=c.privet_markup)

    if answer == "4 отряд":
        states[user] = "4"
        bot.send_message(
            user, d.privet, reply_markup=d.privet_markup)

    if answer == "5 отряд":
        states[user] = "5"
        bot.send_message(
            user, e.privet, reply_markup=e.privet_markup)

    if answer == "6 отряд":
        states[user] = "6"
        bot.send_message(
            user, f.privet, reply_markup=f.privet_markup)


bot.polling(non_stop=True)
