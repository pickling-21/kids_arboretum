from telebot import types

privet = '''Привет! Это 3 район
Твоя задача найти одинокий каменный столб в сосновом бору. 
Он подскажет тебе что делать дальше.'''
privet_markup = types.InlineKeyboardMarkup()
privet_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, я найду", callback_data="сосновый бор")
privet_markup.add(privet_markup_btn1)
