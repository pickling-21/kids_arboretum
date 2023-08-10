from secret import *
from telebot import types

privet_picture = 'https://imageup.ru/img12/4471025/kandinsky-download-1691707448138.jpg'

privet = '''_Приветствуем вас, детективы, на пороге мистических тайн и неведомых путей! Вступай в наши ряды, где тьма и свет переплетаются, а загадки таинственно разгадываются.
Направь свои шаги туда, где отсутствует красная стрелка и история откроется перед тобой.
Добро пожаловать в первый район тайн!_'''

ex = '''Вам нужно будет находить QR-коды, которые скрывают в себе ключевые слова. После сканирования QR-кода вы получите слово, которое нужно будет отправить в чат. '''

сhoice = 'У вас есть два варианта, вколоть белке антидот, но неизвестно поможет ли он ей. Или не вкалывать.'

choice_markup = types.InlineKeyboardMarkup(row_width=1)  # создать клавиватуру
choice_markup_btn1 = types.InlineKeyboardButton(
    text="Да, я попробую помочь ей", callback_data="1 да")  # создваем кнопку
choice_markup_btn2 = types.InlineKeyboardButton(
    text="Нет, она совершила слишком много зла", callback_data="1 нет")
choice_markup.add(choice_markup_btn1, choice_markup_btn2)

good_end = 'Вы спасли белку, скоро она вернется в свой человеческий облик и попробует вернуть все на свои места'

bad_end = 'Хм? Вы решили её не спасать? Ладно это ваш выбор, белка окончательно потеряла рассудок и убежала в лес грызть орехи и творить злые дела.'
hosta = 'На cледущей локации все легко и просто, около пруда вам поможет растение...'

end_markup = types.InlineKeyboardMarkup(row_width=1)
end_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться к выбору квеста", callback_data="вернуться")
end_markup.add(end_markup_btn1)


def send_text(user, text):
    if text.lower() == 'бабушка':
        bot.send_message(
            user, '[Бабушка расскажет вам историю](https://youtu.be/3cXz94-QdFk)', parse_mode='Markdown')
        bot.send_message(user, hosta)
        states[user] = '1.1'
    if text.lower() == 'хоста' and states[user] == '1.1':
        bot.send_message(
            user, '[Кадры](https://youtu.be/Fk83UPkFSOc) сделаны на месте где последний раз видели белку', parse_mode='Markdown')
        states[user] = '1.2'
    if text.lower() == 'белка' and states[user] == '1.2':
        bot.send_message(
            user, '[Момент когда к белке возвращается рассудок](https://youtu.be/VTdYoqoVG7Q)', parse_mode='Markdown')
        states[user] = '1.3'
    if text.lower() == 'гриб':
        bot.send_message(user, 'Грибочик :] ')
        bot.send_message(
            user, '[Получена ачивка "Глазастый" :)](https://youtu.be/Lxd6sHpqmOg)', parse_mode='Markdown')
    if text.lower() == 'погоня' and states[user] == '1.3':
        bot.send_message(
            user, '[Погоня за белкой](https://youtu.be/PwYM8MGjYgg)', parse_mode='Markdown')
        states[user] = '1.4'
    if text.lower() == 'лесник' and states[user] == '1.4':
        bot.send_message(user, сhoice, reply_markup=choice_markup)


def send_query(user, answer):
    if answer == "1 отряд":
        states[user] = "1"
        bot.send_photo(user, privet_picture)
        bot.send_message(
            user, privet, parse_mode='Markdown')
        bot.send_message(
            user, ex, parse_mode='Markdown')
    if answer == '1 да':
        bot.send_message(user, good_end)
        bot.send_message(
            user, '[Видео](https://youtu.be/pSRljsbIITs)', parse_mode='Markdown', reply_markup=end_markup)
    if answer == '1 нет':
        bot.send_message(user, bad_end)
        bot.send_message(
            user, '[Видео](https://youtu.be/Il9irENp7aY)', parse_mode='Markdown', reply_markup=end_markup)

    if answer == 'вернуться':
        states[user] = 0
