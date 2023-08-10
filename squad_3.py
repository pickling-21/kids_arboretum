from telebot import types
from secret import *

pictures = {
    1: "https://imageup.ru/img94/4469301/kandinsky-download-1691565741225-1.jpg",  # столб
    2: 'https://imageup.ru/img118/4470607/kandinsky-download-1691681324429.jpg',  # жара
    3: 'https://imageup.ru/img252/4469318/kandinsky-download-1691566387079.jpg',  # белка
    4: 'https://imageup.ru/img116/4469304/kandinsky-download-1691566318035-1.jpg',  # бегемот
    5: 'https://imageup.ru/img186/4470629/kandinsky-download-1691682424374.jpg',  # мороженое
    6: 'https://imageup.ru/img263/4469365/kandinsky-download-1691646296309.jpg',  # веер
    7: "https://imageup.ru/img153/4469364/kandinsky-download-1691646332765.jpg",  # холодильник
    8: 'https://imageup.ru/img236/4469294/kandinsky-download-1691315122299.jpg',  # вода
}
privet = '''Привет! Это 3 район
Твоя задача найти одинокий каменный столб в сосновом бору. 
Он подскажет тебе что делать дальше. 
Когда дойдешь, столб тебе расскажет свое предназначение. Пришли его ответным сообщением.'''
# privet_markup = types.InlineKeyboardMarkup()
# privet_markup_btn1 = types.InlineKeyboardButton(
#     text="Я ввел", callback_data="ввел")
# privet_markup.add(privet_markup_btn1)


global_warm = '''Ты нашел наш камень силы. Вы оказались в сказочном лесу, где животные могут разговаривать. Из-за глобального потепления животные в нашем лесу стали вести себя странно, пожалуйста, помогите нам вернуть их в нормальное состояние. '''
global_warm_markup = types.InlineKeyboardMarkup(row_width=1)
global_warm_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, с радостью помогу", callback_data="1 поможет")
global_warm_markup_btn2 = types.InlineKeyboardButton(
    text="Нет, мне лень, я хочу спать", callback_data='2 плохая концовка')
global_warm_markup_btn3 = types.InlineKeyboardButton(
    text="Расскажите подробнее про глобальное потепление", callback_data="3 глобальное потепление")
global_warm_markup.add(global_warm_markup_btn1,
                       global_warm_markup_btn2, global_warm_markup_btn3)

bad = " :( Ну и все. Игра закончена"
warming = '''*Глобальное потепление: Причины и Влияние*

*Глобальное потепление* – это явление повышения средней температуры Земли на поверхности. Этот процесс имеет серьезные последствия для природы и общества. Вот некоторые из главных причин, вызывающих глобальное потепление:

*Промышленная деятельность*, сжигание топлив способствуют выделению парниковых газов, таких как углекислый газ (CO2), метан (CH4) и оксид азота (N2O) в атмосферу. Эти газы создают эффект парникового эффекта, удерживая тепло и повышая температуру.

Также причинами являются:
Уничтожение лесов
Изменение земельного использования
Промышленная деятельность

Для борьбы с глобальным потеплением важно принимать меры по снижению выбросов парниковых газов, поощрять устойчивое землепользование, инвестировать в возобновляемую энергетику и повышать осведомленность об этой проблеме среди общества.'''

next = '''Скорлупа от орешек приведет вас к белке, которой очень нужна помощь.'''
next_markup = types.InlineKeyboardMarkup(row_width=1)
next_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, я нашел ее", callback_data="белка")
next_markup.add(next_markup_btn1)


back_markup = types.InlineKeyboardMarkup(row_width=1)
back_markup_btn1 = types.InlineKeyboardButton(
    text="вернуться", callback_data="назад 2")

belka_more = '''_В тихом лесу, где шепчутся деревья и ручей песню поёт, одинокая белка Рыжуля смотрит вдаль, глаза её полны тоски и скуки. В её сердце таится тайна, которую даже сам лес не знает. Она жаждет оживить свои дни, найти свой путь в этом мире._'''
belka = "Привет! Я белка Рыжуля. Мне скучно. Пожалуйста, станцуй для меня под эту музыку и пришли мне видео танца, но короткое, максимум 15 секунд."

thanks = "Спасибо, очень крутой танец"
thanks_markup = types.InlineKeyboardMarkup(row_width=1)
thanks_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, куда дальше?", callback_data="танец белка")
thanks_markup.add(thanks_markup_btn1)


belka_to_begemot = '''Спасибо тебе, я чувствую себя лучше. Ой, а как же Федя? Он мой друг, помоги ему, пожалуйста! В последний раз я видела его около чебурашки. Как найдешь его, напиши, пожалуйста, в чем сидит Федя, и он с тобой поговорит. _(существительное в именительном падеже)_'''
begemot = '''О привет! Я — бегемот Федя, и мне оооочень жарко! Так жарко, что я забрался в холодильник. Помогите мне, пожалуйста. Мммм… сейчас бы мороженки! Кажется я слышал, где-то пели песню про мороженое, может там его и получить можно. '''

pro_begemota = '_Феде нужно найти несколько вещей, чтобы охладится. После выполнения каждого задания вы получите подсказку, где лежит предмет. На каждом найденном предмете будет буква, которую нужно будет отправить в чат. Если буква будет верная, то тогда вы получите предмет._'''

pro_begemota_markup = types.InlineKeyboardMarkup(row_width=1)
pro_begemota_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, я понял. Что нужно делать?", callback_data="дальше")
pro_begemota_markup.add(pro_begemota_markup_btn1)

moroz_ex = '''Чтобы получить мороженое, напишите свой любимый вкус мороженого.'''

moroz = 'Мороженое вы можете найти в клубе. После того как найдете, пришлите букву.'

moroz_done = '''Спасибо, стало лучше… но было бы замечательно, если бы еще веер придал этому какое-то особенное движение.'''

veer_ex = '''Хочется какой-то сказки. Знаете, я недавно слышал сказку о приключениях девочки, которая нашла волшебный веер. Она совершила много чудес, когда она размахивала этим веером и изменила очень сильно свою жизнь и жизнь окружающих ее людей. Расскажите, пожалуйста, какие добрые дела вы бы сделали, если бы у вас был волшебный веер. Для этого запишите голосовое сообщение на примерно 20 секунд'''

veer = '''Как много хороших дел! Веер вы можете найти там, где обитают другие сказки'''

veer_done = '''Ого, уже не так жарко, но, знаешь, почему-то захотелось попить…'''

voda_ex = '''Напишите ассоциацию на каждую букву в слове "ВОДА"'''

voda = 'Вода находится в чебурашке.'

end_11 = '''Вау, вы нашли все что мне нужно и помогли мне справится с жарой. Спасибо вам! Я пожалуй, еще посижу в холодильнике, а вы идите дальше. Кажется, у второго района есть что-то интересное для вас. Тоже как-то связано с бутылками.'''
end_markup = types.InlineKeyboardMarkup(row_width=1)
end_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться к выбору квеста", callback_data="вернуться")
end_markup.add(end_markup_btn1)


def send_query(user, answer):
    # 3 район
    if answer == "3 отряд" or states[user] == "3":
        curr_squad = 3
        states[user] = "3"
        bot.send_message(
            user, privet)

    if states[user] == 'столб':
        states[user] = "бор"

    if answer == '1 поможет':
        states[user] = "1 помощь"
        bot.send_message(user, next, reply_markup=next_markup)

    if answer == 'белка':
        states[user] = '3 белка'
        bot.send_message(user, pictures[3])
        bot.send_message(user, belka_more, parse_mode='Markdown')
        bot.send_message(user, belka)
        bot.send_audio(user, 'https://psv4.vkuseraudio.net/s/v1/amp2/HXGfJ1Gh-aHnhpM7vjlKI_Zl8vWgEExjKvj81St1uzNVVxpy9qK7YXUhNV-P0LM_w785HPXYP9nP5a_ej05acLYdUlQbV4QaIy51iXN8p8rASkIue5IA8MRkR6St4VvD8x9iVJbV06HLCZujBveS5ELW6tPYqjgP0v5u.mp3?siren=1')

    if answer == '2 плохая концовка':
        states[user] = "3 злой"
        bot.send_message(
            user, bad)

    if answer == '3 глобальное потепление':
        states[user] = "3 потепление"
        bot.send_photo(user, pictures[2])

        bot.send_message(
            user, warming, parse_mode='Markdown')

    if answer == 'дальше':
        bot.send_photo(user, pictures[5])
        bot.send_message(user, moroz_ex)
        states[user] = 'з мороженое'

    if answer == "назад 2":
        states[user] = "бор"

    if states[user] == "1 видио есть":
        bot.send_message(
            user, belka_to_begemot, parse_mode='Markdown')
        states[user] = 'ждем холодильник'


def send_text(user, text):
    end = True
    if text.lower() == 'сила' and states[user] == '3':
        states[user] = 'столб'
        bot.send_photo(user, pictures[1])
        bot.send_message(
            user, global_warm, reply_markup=global_warm_markup)

    elif text.lower() == 'холодильник' and states[user] == 'ждем холодильник':
        bot.send_photo(user, pictures[4])
        bot.send_message(user, begemot)
        bot.send_message(user, pro_begemota, parse_mode='Markdown',
                         reply_markup=pro_begemota_markup)

    elif states[user] == 'з мороженое':
        bot.send_message(user, moroz)
        states[user] = 'ждем мороженое'

    elif text.lower() == 'л' and states[user] == 'ждем мороженое':
        bot.send_message(user, moroz_done)
        bot.send_photo(user, pictures[6])
        bot.send_message(user, veer_ex)
        states[user] = 'ждем веер'

    elif text.lower() == 'е' and states[user] == 'веер':
        bot.send_message(user, veer_done)
        bot.send_message(user, pictures[8])
        bot.send_message(user, voda_ex)
        states[user] = 'ждем воду'

    elif states[user] == 'ждем воду':
        bot.send_message(user, voda)
        states[user] = 'вода'

    elif text.lower() == 'с' and states[user] == 'вода':
        bot.send_message(user, end_11, reply_markup=end_markup)
        states[user] = '3 все'

    else:
        return False
