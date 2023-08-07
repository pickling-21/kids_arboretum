from telebot import types

privet = '''5 район хочет вам показать нечто интересное. Вам нужно будет написать в ответном сообщении, что у них за место, а чайка вам подскажет'''

privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="окей", callback_data="столовка")
privet_markup.add(privet_markup_btn1)
