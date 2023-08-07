from telebot import types

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
    text="Нет, мне лень, я хочу спать", callback_data="2 плохая")
global_warm_markup_btn3 = types.InlineKeyboardButton(
    text="Расскажите подробнее про глобальное потепление", callback_data="3 глобальное потепление")
global_warm_markup.add(global_warm_markup_btn1,
                       global_warm_markup_btn2, global_warm_markup_btn3)

bad = "Ну и все. Игра закончена"
warming = 'Текст про глобальное потепление'

next = '''Скорлупа от орешек приведет вас к белке, которой очень нужна помощь.'''
next_markup = types.InlineKeyboardMarkup(row_width=1)
next_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, я нашел ее", callback_data="белка")
next_markup.add(next_markup_btn1)

back_markup = types.InlineKeyboardMarkup(row_width=1)
back_markup_btn1 = types.InlineKeyboardButton(
    text="вернуться", callback_data="назад 2")

belka_more = '''_В тихом лесу, где шепчутся деревья и ручей песню поёт, одинокая белка Рыжуля смотрит вдаль, глаза её полны тоски и скуки. В её сердце таится тайна, которую даже сам лес не знает. Она жаждет оживить свои дни, найти свой путь в этом мире._'''
belka = "Привет, я белка. Мне скучно, и жарко. Пожалуйста, станцуй для меня."
begemot = "Как же жарко! О, привет! Я бегемот Федя, из-за жары я забрался в холодильник. Чтобы выбраться мне нужно что-то холодное, чтобы мне было не жарко на улице."
