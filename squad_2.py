from telebot import types

privet = '''Это второй'''
privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="1. 1 ответ", callback_data="1 ответ")
privet_markup_btn2 = types.InlineKeyboardButton(
    text="2. 2 ответ", callback_data="2 ответ")
privet_markup_btn3 = types.InlineKeyboardButton(
    text="3. 2 ответ", callback_data="3 ответ")
privet_markup.add(privet_markup_btn1,
                  privet_markup_btn2, privet_markup_btn3)
