from telebot import types
from secret import *

privet = '''Здравствуйте!
Вам нужно найти чайку, и она подскажет вам ключевое слово. Введите его в чат.  
'''
b = 'Вы зашли в место для дендропарка, я покажу вам как он будет выглядеть в будущем.'
b_markup = types.InlineKeyboardMarkup(row_width=1)
b_markup_btn1 = types.InlineKeyboardButton(
    text="Отлично! Что у вас тут есть?", callback_data="2")
b_markup.add(b_markup_btn1)

c = '''Справа от тебя будет чистейший фонтан, он будет расслаблять своим журчанием. Найдите монетку на этом месте и подбросьте ее, загадав при этом желание. Если выпадет орел, то желание сбудется. '''
с_markup = types.InlineKeyboardMarkup(row_width=1)
с_markup_btn1 = types.InlineKeyboardButton(
    text="Да, у меня сбудется желание!", callback_data="3")
с_markup_btn2 = types.InlineKeyboardButton(
    text="Жаль, но в следующий раз обязательно получится", callback_data="3")
с_markup.add(с_markup_btn1, с_markup_btn2)

d = '''Слева будет сад камней. Он будет полностью из камней! Сядьте на траву и насладитесь тишиной сада. Послушайте эту расслабляющую музыку. '''
d_markup = types.InlineKeyboardMarkup(row_width=1)
d_markup_btn1 = types.InlineKeyboardButton(
    text="Ох, меня отпустило напряжение", callback_data="4")
d_markup.add(с_markup_btn1)


e = '''Пройдите дальше и вы наткнетесь на пруд с рыбками.  Вокруг него будет японский сад. Попробуйте повторить движение воды и придумайте танец ручейка. Пришлите нам видео, чтобы мы тоже посмотрели! Если вас больше 5 человек можете поиграть в ручеек. Такое видео мы тоже примем.'''
e_markup = types.InlineKeyboardMarkup(row_width=1)
e_markup_btn1 = types.InlineKeyboardButton(
    text="Ох, меня отпустило напряжение", callback_data="3")
e_markup.add(e_markup_btn1)


e_2 = '''Нужно встать в «ручеек», то есть поделиться на пары, и, держась за руки, поднять их вверх. Кому пары не достанется, то тот станет водящим. Его задача – пройтись по длинному «живому» коридору и выбрать себе напарника. Новая пара встает в конец «потока». А тот, у кого забрали друга, ищет ему замену – теперь его очередь выбирать!'''

f = '''Вы наверно уже увидели большую чайку, которая смотрит на вас. Чтобы не забыть про нее сделайте с ней селфи и выложите ее у себя в соцсетях, а также не забудьте прислать нам'''


def send_query(user, answer):
    if answer == "5 отряд":
        states[user] = "a"
        bot.send_message(
            user, privet)


def send_text(user, text):
    if text.lower() == 'дендропарк':
        bot.send_message(user, b, b_markup)
