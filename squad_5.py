from telebot import types

privet = '''Это пятый'''

privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="окей", callback_data="столовка")
privet_markup.add(privet_markup_btn1)
