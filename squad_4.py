from telebot import types
from secret import *

pictures = {
    1: 'https://imageup.ru/img168/4469380/kandinsky-download-1691646268525.jpg',
    2: 'https://imageup.ru/img57/4469369/kandinsky-download-1691645326194.jpg',
    3: 'https://imageup.ru/img44/4469378/kandinsky-download-1691645795939.jpg',
    4: 'https://imageup.ru/img300/4469371/kandinsky-download-1691645566909.jpg',
    5: 'https://imageup.ru/img82/4470950/kandinsky-download-1691700015496.jpg'
}

privet = '''Привет, путник. Нам нужна твоя помощь. Отправляйся к большой красной рыбе, там ты увидишь название миссии. И помни, что времени мало. Удачи.

*Отправь мне самое короткое слово из названия миссии* 

Только после того как ты напишиешь мне это слово, рыба тебе расскажет, что случилось.
'''

privet_markup = types.InlineKeyboardMarkup()  # создаем клавиатуру
privet_markup_btn1 = types.InlineKeyboardButton(
    text="Миссию принял", callback_data="операция рад")
# создаем кнопку
privet_markup.add(privet_markup_btn1)
# добавить кнопку на клавиатуру

riba = '''_Привет, друзья! Я в отчаянии и нуждаюсь в вашей помощи. Всё стало совершенно невероятным! Вы не поверите, но я, на самом деле, чайка. Но, по какой-то неведомой причине, я тут, застряла в железной рыбе, а не летаю по небу.
Это невероятная история началась после того, как вода в нашем родном заливе стала изменяться. Оказывается, на местном заводе начались выбросы вредных радиационных веществ, и они попали в воду. Все это нездоровое вещество перемешалось с водой, и я, будучи обычной чайкой, попила эту загрязненную воду и через время стала рыбой._'''
riba_2 = '''_Теперь, чтобы вернуться в прежний облик, мне нужен _*антирадин.*_ Это вещество, которое очистит мой организм, и я снова стану чайкой._'''
riba_2_markup = types.InlineKeyboardMarkup(row_width=1)
riba_2_btn1 = types.InlineKeyboardButton(
    text="Может ты подскажешь где его искать?", callback_data="антирадин")
riba_2_markup.add(riba_2_btn1)


bad_end = 'Ну вот и все... Останусь я до конца дней своих рыбой. Грустно, грустно...'
bad_end_markup = types.InlineKeyboardMarkup(row_width=1)
bad_end_btn1 = types.InlineKeyboardButton(
    text="Мне лень", callback_data="лень")
bad_end_btn2 = types.InlineKeyboardButton(
    text="Я помогу!", callback_data="окей")
bad_end_markup.add(bad_end_btn1, bad_end_btn2)

basket_1 = 'У меня есть записка, которая поможет найти антирадин. Но там только какие-то термины, которые я не понимаю. *Пожалуйста, передайте мне ответ на эту загадку через сообщение.*'
basket = '''*Биоразнообразие
Атмосфера
Солнечная энергия
Компостирование
Естество
Токсичность 
Биопластик
Отходы
Лесозаготовка*'''


ras = '''*Биоразнообразие*: Это многообразие живых организмов на Земле в рамках экосистем, включая разнообразие видов растений, животных и микроорганизмов.

*Атмосфера*: Это слой газов, окружающий Землю, включающий кислород, азот, углекислый газ и другие составляющие, которые поддерживают жизнь на планете.

*Солнечная энергия*: Это энергия, получаемая от солнечного света и преобразуемая в электричество или тепло, используемое для энергетических нужд.

*Компостирование*: Это процесс разложения органических отходов в компост, который затем может использоваться как удобрение для почвы.

*Естество*: Это синоним слова "природа", означающий все живущие и неживущие элементы окружающей среды.

*Токсичность*: Это свойство вещества вызывать вредные эффекты на здоровье живых организмов при контакте или воздействии.

*Биопластик*: Это вид пластика, производимого из биологически разлагаемых материалов, что делает его более экологически безопасным.

*Отходы*: Это материалы, которые больше не могут быть использованы и требуют специальной обработки, чтобы минимизировать их негативное влияние на окружающую среду.

*Лесозаготовка*: Это процесс сбора древесины из леса с целью использования её в различных промышленных процессах и строительстве.'''

ras_markup = types.InlineKeyboardMarkup()
ras_markup_btn1 = types.InlineKeyboardButton(
    text="Спасибо, сейчас пришлю разгадку", callback_data="пошел к кольцу")
ras_markup.add(ras_markup_btn1)

basket_markup = types.InlineKeyboardMarkup(row_width=1)
basket_markup_btn1 = types.InlineKeyboardButton(
    text="Хочу узнать, что значат эти термины", callback_data="рас")
basket_markup_btn2 = types.InlineKeyboardButton(
    text="Я понял куда идти, сейчас пришлю ответ", callback_data="пошел к кольцу")
basket_markup.add(basket_markup_btn1, basket_markup_btn2)

radin = '''Молодец, думаю, ты найдешь там антирадин. Сфотографируй его и пришли в чат, так он окажется у тебя в инвентаре. После тебе нужно будет подойти к рыбе и передать его ей.'''

photo = '_*Антирадин у тебя в инвентаре.*_'
riba_go = 'Теперь тебе нужно дойти обратно до рыбы.'
riba_go_markup = types.InlineKeyboardMarkup(row_width=1)
riba_go_markup_btn1 = types.InlineKeyboardButton(
    text="Я дошел", callback_data="обратно")
riba_go_markup.add(riba_go_markup_btn1)


end = '_Прекрасно вернуться к небу! Спасибо антирадину за метаморфозу. Спасибо тебе! Теперь ветер под крыльями – моя свобода!_'
end_markup = types.InlineKeyboardMarkup(row_width=1)
end_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться к выбору квеста", callback_data="вернуться")
end_markup.add(end_markup_btn1)


def send_text(user, text):
    end = True
    if text.lower() == 'рад' and states[user] == "4":
        bot.send_photo(user, pictures[1])
        bot.send_message(user, riba, parse_mode='Markdown',
                         reply_markup=bad_end_markup)

    elif text.lower() == 'баскетбол' and states[user] == "баскет":
        bot.send_message(user, radin, parse_mode='Markdown')
        states[user] = '4 ждем фото'
    else:
        end = False

    return end


def send_query(user, answer):
    if answer == "4 отряд":
        curr_squad = 4
        states[user] = "4"
        bot.send_photo(user, pictures[5])
        bot.send_message(
            user, privet, parse_mode='Markdown')

    if answer == "лень":
        bot.send_message(user, bad_end)

    if answer == 'окей':
        bot.send_photo(user, pictures[2])
        bot.send_message(user, riba_2, parse_mode='Markdown',
                         reply_markup=riba_2_markup)
        states[user] = 'баскет'

    if answer == 'антирадин':
        bot.send_message(user, basket_1, parse_mode='Markdown')
        bot.send_photo(user, pictures[3])
        bot.send_message(user, basket, parse_mode='Markdown',
                         reply_markup=basket_markup)

    if answer == 'рас':
        bot.send_message(user, ras, reply_markup=ras_markup,
                         parse_mode='Markdown')
        states[user] = "4"

    if answer == 'пошел к кольцу':
        states[user] = 'баскет'

    if answer == 'обратно':
        bot.send_photo(user, pictures[4])
        bot.send_message(user, end, reply_markup=end_markup,
                         parse_mode='Markdown')

    if answer == 'вернуться':
        states[user] = 0


def send_photo(user):
    if states[user] == '4 ждем фото':
        bot.send_message(user, photo, parse_mode='Markdown')
        bot.send_message(
            user, riba_go, reply_markup=riba_go_markup, parse_mode='Markdown')
