
from telebot import TeleBot, types
from random import randint
# токен для бота
token = "6365845419:AAGzeRqMSyEFhoGQwJ4pdFd5f-R0kvGjtSI"

# словарь картинок для квеста
pictures = {
    0: "https://storage.geekclass.ru/images/760e484b-a099-4a7a-a722-5aec9a933614.jpg",
    1: "https://storage.geekclass.ru/images/4637fc41-08df-466a-b112-aa577dba6c1d.jpg",
    2: "https://storage.geekclass.ru/images/c2a2a60c-9c7b-4c3a-b663-42d2559bf869.jpg"
}

states = {}
inventories = {}
bot = TeleBot(token)

@bot.message_handler(commands=["start"])
def start_game(message):
    user = message.chat.id

    states[user] = 0
    inventories[user] = []

    bot.send_message(user, "Добро пожаловать в игру!")

    process_state(user, states[user], inventories[user])

@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    process_answer(user, call.data)

def process_state(user, state, inventory):
    kb = types.InlineKeyboardMarkup()

    bot.send_photo(user, pictures[state])

    if state == 0:
        kb.add(types.InlineKeyboardButton(text="пойти направо", callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="пойти налево", callback_data="2"))

        bot.send_message(user, "Вы в оказались в темном подземелье, перед вами два прохода.", reply_markup=kb)

    if state == 1:
        kb.add(types.InlineKeyboardButton(text="переплыть", callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="вернуться", callback_data="2"))

        bot.send_message(user, "Перед вами большое подземное озеро, а вдали виднеется маленький остров.", reply_markup=kb)

    if state == 2:
        bot.send_message(user, "Вы выиграли.")

def process_answer(user, answer):
    if states[user] == 0:
        if answer == "1":
            states[user] = 1
        else:
            if "key" in inventories[user]:
                bot.send_message(user,
                                 "Перед вами закрытая дверь. Вы пробуете открыть ее ключем, и дверь поддается. Кажется, это выход.")
                states[user] = 2
            else:
                bot.send_message(user, "Перед вами закрытая дверь, и, кажется, без ключа ее не открыть. Придется вернуться обратно.")
                states[user] = 0

    elif states[user] == 1:
        if answer == "2":
            bot.send_message(user,
                             "И правда, не стоит штурмовать неизвестные воды. Возвращаемся назад...")
            states[user] = 0
        else:
            bot.send_message(user,
                             "Вы пробуете переплыть озеро...")

            chance = randint(0,10)
            if chance == 4:
                bot.send_message(user,
                                 "Вода оказалось теплой, а в сундуке на острове вы нашли старый ключ. Стоит вернутся обратно.")
                inventories[user].append("key")
                states[user] = 0
            else:
                bot.send_message(user,
                                 "На середине озера вас подхватывают волны и возвращают обратно.")
                states[user] = 1

    process_state(user, states[user], inventories[user])

bot.polling(none_stop=True)