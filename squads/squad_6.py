from squads.data import *
from telebot import types

privet = '''Привет дорогой друг!
Нам срочно нужно собраться в беседке Екатеринбурга. Случилась беда в городе “Чайка” и нам нужна твоя помощь. Подробности узнаешь  на месте. 
'''

privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, я сейчас буду", callback_data="монстры")
privet_markup.add(privet_markup_btn1)

kod = '''Как придешь, сообщи код доступа. Ты его сразу увидишь, вроде его оставили на столе.'''

kod_2 = "*Код правильный*"
musor = '''Этот город заражается мусором. Животные из-за мусора погибают. Можешь ли ты помочь нам, остановить мусорных монстров и спасти животных.  Но нам нужно найти инструменты, чтобы справится с мусором. Раньше инструменты лежали в одном месте, но потом пришли мусорные монстры, сломали стены у беседки и разбросали наши инструменты. Помогите нам их собрать.'''
musor_markup = types.InlineKeyboardMarkup(row_width=1)
musor_markup_btn1 = types.InlineKeyboardButton(
    text="Узнать подробнее про проблему мусора", callback_data="6 подробнее")
musor_markup_btn2 = types.InlineKeyboardButton(
    text="Узнать подробнее про задание", callback_data="6 задание")
musor_markup_btn3 = types.InlineKeyboardButton(
    text="Слово составлено", callback_data="6 сделано")
musor_markup.add(musor_markup_btn1, musor_markup_btn2, musor_markup_btn3)

ex = '''Задание:
_На каждом инструменте есть буква. Чтобы мы добавили инструменты в инвентарь, вам нужно будет составить из этих букв правильное слово и прислать его в чат._'''

musor_text = '''Пластик и металлические отходы, а также другой мусор, попадая в природу, могут стать пищей для животных, вызывая задыхание или повреждение пищеварительной системы.

Мусорные предметы, вроде пластиковых упаковок и сетей, могут запутываться вокруг животных, причиняя травмы и ограничивая их движение.

Морские животные могут пострадать от пластиковых отходов и микропластика в водах, путая их с пищей или получая травмы.'''

back_markup = types.InlineKeyboardMarkup()
back_markup.add(musor_markup_btn3)

ex_markup = types.InlineKeyboardMarkup()
ex_markup.add(musor_markup_btn3)

start_fight = "Молодцы, вы собрали все инструменты! Теперь мы можем победить мусорных монстров, которые захватили бедных животных."
fight_markup = types.InlineKeyboardMarkup()
fight_markup_btn1 = types.InlineKeyboardButton(
    text='Применить все инструменты', callback_data="победа")
fight_markup.add(fight_markup_btn1)


end = 'Ура! Мы победили! Животные спасены! '
end_markup = types.InlineKeyboardMarkup(row_width=1)
end_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться к выбору квеста", callback_data="вернуться")
end_markup.add(end_markup_btn1)

# fight = 'Выбери инструмент'
# a = 'Тряпка'
# b = 'Швабра'
# c = 'Метла'
# d = 'Пылесос'
# e = 'Мусорный пакет'
# fight_markup = types.InlineKeyboardMarkup()
# fight_markup_btn1 = types.InlineKeyboardButton(
#     text=a, callback_data="a")
# fight_markup_btn2 = types.InlineKeyboardButton(
#     text=b, callback_data="b")
# fight_markup_btn3 = types.InlineKeyboardButton(
#     text=c, callback_data="c")
# fight_markup_btn4 = types.InlineKeyboardButton(
#     text=d, callback_data="d")
# fight_markup_btn5 = types.InlineKeyboardButton(
#     text=d, callback_data="e")
# fight_markup.add(fight_markup_btn1, fight_markup_btn2,
#                  fight_markup_btn3, fight_markup_btn4, fight_markup_btn5)


pictures = {
    1: 'https://imageup.ru/img97/4471020/kandinsky-download-1691706303017.jpg',
    2: 'https://imageup.ru/img215/4471021/kandinsky-download-1691706435793.jpg',
    3: 'https://imageup.ru/img27/4469360/kandinsky-download-1691645811801.jpg',
    4: 'https://imageup.ru/img232/4471022/kandinsky-download-1691706511559.jpg',
    5: 'https://imageup.ru/img250/4469361/kandinsky-download-1691645857784.jpg',
    6: 'https://imageup.ru/img47/4469363/kandinsky-download-1691646072636.jpg'

}


def send_text(user, text):
    if text == '6143':
        bot.send_photo(user, pictures[2])
        bot.send_message(user, kod_2, parse_mode='Markdown')
        bot.send_photo(user, pictures[3])
        bot.send_message(user, musor, reply_markup=musor_markup)

    if text.lower() == 'земля' and states[user] == '6 ждем слово':
        bot.send_photo(user, pictures[5])
        bot.send_message(user, start_fight, reply_markup=fight_markup)


def send_query(user, answer):
    if answer == "6 отряд":
        curr_squad = 6
        states[user] = "6"
        bot.send_photo(user, pictures[1])
        bot.send_message(
            user, privet, reply_markup=privet_markup)

    if answer == 'монстры':
        bot.send_message(user, kod)

    if answer == '6 подробнее':
        bot.send_message(user, pictures[4])
        bot.send_message(user, musor_text, reply_markup=back_markup)

    if answer == '6 задание':
        bot.send_message(user, ex, reply_markup=ex_markup,
                         parse_mode='Markdown')

    if answer == 'победа':
        bot.send_photo(user, pictures[6])
        bot.send_message(user, end, reply_markup=end_markup)

    if answer == '6 сделано':
        bot.send_message(user, "Пришли слово в чат.")
        states[user] = '6 ждем слово'

    if answer == 'вернуться':
        states[user] = 0
