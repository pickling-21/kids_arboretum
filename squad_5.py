from telebot import types
from secret import *

privet = '''Здравствуйте!
Вам нужно найти чайку, и она подскажет вам ключевое слово. Введите его в чат.  
'''
b = 'Вы зашли в место для дендропарка, я покажу вам как он будет выглядеть в будущем.'
b_markup = types.InlineKeyboardMarkup(row_width=1)
b_markup_btn1 = types.InlineKeyboardButton(
    text="Отлично! Куда дальше?", callback_data="2")
b_markup.add(b_markup_btn1)

c = '''Справа от тебя будет чистейший фонтан, он будет расслаблять своим журчанием. Найдите монетку на этом месте и подбросьте ее, загадав при этом желание. Если выпадет орел, то желание сбудется. '''
с_markup = types.InlineKeyboardMarkup(row_width=1)
с_markup_btn1 = types.InlineKeyboardButton(
    text="Да, у меня выпал орел!", callback_data="2.2")
с_markup_btn2 = types.InlineKeyboardButton(
    text="Жаль, но у меня выпала решка", callback_data="2.1")
с_markup_btn3 = types.InlineKeyboardButton(
    text="Не нашел монетку :(", callback_data="2.1")
с_markup.add(с_markup_btn1, с_markup_btn2, с_markup_btn3)

с_plus = 'Не расстраивайся, лучше сходи в сад камней'
с_plus_markup = types.InlineKeyboardMarkup(row_width=1)
с_plus_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо", callback_data="3")
с_plus_markup.add(с_plus_markup_btn1)

с_plus_2 = 'Поздравляю! Пойдем в сад камней'
с_plus_2_markup = types.InlineKeyboardMarkup(row_width=1)
с_plus_2_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо", callback_data="3")
с_plus_2_markup.add(с_plus_2_markup_btn1)

d = '''Слева будет сад камней. Он будет полностью из камней! Сядьте на траву и насладитесь тишиной сада. Послушайте эту расслабляющую музыку. '''
d_markup = types.InlineKeyboardMarkup(row_width=1)
d_markup_btn1 = types.InlineKeyboardButton(
    text="Ох, меня отпустило, стало легче.", callback_data="4")
d_markup.add(d_markup_btn1)


e = '''Пройдите дальше и вы наткнетесь на пруд с рыбками.  Вокруг него будет японский сад. Попробуйте повторить движение воды и придумайте танец ручейка. Пришлите нам видео кружок, чтобы мы тоже посмотрели! Если вас больше 5 человек можете поиграть в ручеек. Такое видео мы тоже примем.
Но видео должно быть не дольше 15 секунд. Также можно прислать видеокружок.
'''
e_markup = types.InlineKeyboardMarkup(row_width=1)
e_markup_btn1 = types.InlineKeyboardButton(
    text="Как играть в ручеек?", callback_data="4.1")
e_markup.add(e_markup_btn1)


e_1 = '''Нужно встать в «ручеек», то есть поделиться на пары, и, держась за руки, поднять их вверх. Кому пары не достанется, то тот станет водящим. Его задача – пройтись по длинному «живому» коридору и выбрать себе напарника. Новая пара встает в конец «потока». А тот, у кого забрали друга, ищет ему замену – теперь его очередь выбирать!'''
e_1_markup = types.InlineKeyboardMarkup(row_width=1)
e_1_markup_btn1 = types.InlineKeyboardButton(
    text="Спасибо, сейчас пришлю видео", callback_data="5")
e_1_markup.add(e_1_markup_btn1)

e_2 = 'Вау, вот это видео'

f = '''Вы наверно уже увидели большую чайку, которая смотрит на вас. Чтобы не забыть про нее сделайте с ней селфи и выложите ее у себя в соцсетях, а также не забудьте прислать нам'''

f_2 = 'Крутое фото!'

g = '''А теперь давайте подойдем к нашей беседке (трансформаторной будке) в итальянском стиле и попробуем представить себя в Италии. 
Запишите, пожалуйста, голосовое сообщение. В нем должно содержатся пожелание следующей смене. Но только говорить нужно с итальянским акцентом.'''

end = 'На этом наша прогулка окончена. Надеемся в ближайшем будущем этот дендропарк воплотиться в реальность, и вы погуляете по нему вживую. '
end_markup = types.InlineKeyboardMarkup(row_width=1)
end_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться к выбору квеста", callback_data="вернуться")
end_markup.add(end_markup_btn1)

pictures = {
    1: 'https://imageup.ru/img16/4471006/kandinsky-download-1691703025889.jpg',
    2: 'https://imageup.ru/img229/4469315/kandinsky-download-1691567488901.jpg',
    3: 'https://imageup.ru/img241/4471008/kandinsky-download-1691703100268.jpg',
    4: 'https://imageup.ru/img297/4471010/kandinsky-download-1691703609322.jpg',
    5: 'https://imageup.ru/img300/4469371/kandinsky-download-1691645566909.jpg',
    6: 'https://imageup.ru/img144/4471016/kandinsky-download-1691705733404.jpg'
}

audio = 'https://cs3-3v4.vkuseraudio.net/s/v1/acmp/Qff23_jlZy9KdLPBWYw9s7ME6YGw2SysUkNfJJmB_hwYrFwSeOcTO9jtuiaxCY7cGskVRaIgZx9c_tgyy1RhT3UyaS3oJiZnY3j33HsUJyjIo6W6YU6IJcur4VNWf8ZWOHKoS3GNGydo.mp3?siren=1'


def send_voice(user):
    if states[user] == '5 ждем голосовое':
        bot.send_message(user, end, reply_markup=end_markup)


def send_photo(user):
    if states[user] == '5 ждем фото':
        bot.send_message(user, f_2)
        bot.send_photo(user, pictures[6])
        bot.send_message(user, g)
        states[user] = '5 ждем голосовое'


def send_video(user):
    if states[user] == "5 ждем видео":
        bot.send_message(user, e_2)
        bot.send_photo(user, pictures[5])
        bot.send_message(user, f)
        states[user] = '5 ждем фото'


def send_query(user, answer):
    if answer == "5 отряд":
        curr_squad = 5
        states[user] = "a"
        bot.send_message(
            user, privet)
    if answer == '2':
        bot.send_photo(user, pictures[2])
        bot.send_message(user, c, reply_markup=с_markup)

    if answer == '2.1':
        bot.send_message(user, с_plus, reply_markup=с_plus_markup)

    if answer == '2.2':
        bot.send_message(user, с_plus_2, reply_markup=с_plus_2_markup)

    if answer == '3':
        bot.send_photo(user, pictures[3])
        bot.send_audio(user, audio)
        bot.send_message(user, d, reply_markup=d_markup, timeout=60)

    if answer == '4':
        bot.send_photo(user, pictures[4])
        bot.send_message(user, e, reply_markup=e_markup)
        states[user] = '5 ждем видео'

    if answer == '4.1':
        bot.send_message(user, e_1, reply_markup=e_1_markup)
        states[user] = '5 ждем видео'

    if answer == 'вернуться':
        states[user] = 0


def send_text(user, text):
    if text.lower() == 'дендропарк' and states[user] == 'a':
        bot.send_photo(user, pictures[1])
        bot.send_message(user, b, reply_markup=b_markup)
