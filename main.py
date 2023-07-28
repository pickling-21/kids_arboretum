
from telebot import TeleBot, types
from random import randint
# токен для бота
from secret import token
privet_word = "Добро пожаловать в квест"
# словарь картинок для квеста

pictures = {
    0: "https://kmv-tur.org/sites/default/files/node/camp/field_images3/2021-05/be6cf54956661e553242225d536ada4a.jpg",
    1: "https://img.tourister.ru/files/2/1/0/7/2/7/6/1/original.jpg",
    2: "https://img.ixbt.site/live/topics/preview/00/03/75/54/74b9058c4c.jpg",
    3: "https://mylnaya-opera.ru/481-large_default/zagotovka-dlya-dekupazha-nadpis-informaciya.jpg",
    4: "https://mylnaya-opera.ru/481-large_default/zagotovka-dlya-dekupazha-nadpis-informaciya.jpg"}

states = {}
inventories = {}
bot = TeleBot(token)


@bot.message_handler(commands=["start"])
def start_game(message):
    user = message.chat.id
    # получаем уникальный id юзера
    states[user] = 0
    inventories[user] = []

    bot.send_message(user, privet_word)

    process_state(user, states[user], inventories[user])


@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    process_answer(user, call.data)


def process_state(user, state, inventory):
    kb = types.InlineKeyboardMarkup()

    bot.send_photo(user, pictures[state])

    if state == 0:
        # вход
        kb.add(types.InlineKeyboardButton(
            text="пойти в дендропарк", callback_data="1"))
        kb.add(types.InlineKeyboardButton(
            text="пойти к 1 отряду", callback_data="2"))

        bot.send_message(user, "Вы оказались в лагере чайка", reply_markup=kb)

    if state == 1:

        kb.add(types.InlineKeyboardButton(
            text="подойти к фонтану", callback_data="1"))
        kb.add(types.InlineKeyboardButton(
            text="пройти к диджей зоне", callback_data="2"))

        bot.send_message(
            user, "вы в дендропарке", reply_markup=kb)

    if state == 2:
        kb.add(types.InlineKeyboardButton(
            text="ответ 1 диджейr", callback_data="1"))
        kb.add(types.InlineKeyboardButton(
            text="ответ 2 диджейr", callback_data="2"))
        bot.send_message(user, "загадка диджей зона")

    if state == 3:
        kb.add(types.InlineKeyboardButton(
            text="ответ 1 фонтан ff", callback_data="1"))
        kb.add(types.InlineKeyboardButton(
            text="ответ 2 фонтанaa", callback_data="2"))
        bot.send_message(user, "загадка фонтан")

    if state == 4:
        bot.send_message(user, "вы у первого отряда")
        kb.add(types.InlineKeyboardButton(
            text="вернуться", callback_data="2"))


def process_answer(user, answer):
    if states[user] == 0:
        if answer == "1":
            states[user] = 1
            bot.send_message(user, "!!!!!!!!!!!!!!!!1")
        elif answer == "2":
            states[user] = 4

    elif states[user] == 1:
        # если фонтан
        if answer == "1":
            states[user] = 3
        # если диджей зона
        elif answer == "2":
            states[user] = 2

    # elif states[user] == 2:
    #     if answer == "1":
    #         bot.send_message(user,
    #                          "Правильный ответ")
    #     elif answer == "2":
    #         bot.send_message(user,
    #                          "Неправильный ответ")

    # elif states[user] == 3:
    #     if answer == "1":
    #         bot.send_message(user,
    #                          "Правильный ответ")
    #     elif answer == "2":
    #         bot.send_message(user,
    #                          "Неправильный ответ")

    process_state(user, states[user], inventories[user])


bot.polling(none_stop=True)
