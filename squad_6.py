from telebot import types

privet = '''Это 6 отряд'''

privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="6 рад", callback_data="дендропарк")

