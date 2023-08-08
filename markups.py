from telebot import types

start_markup = types.InlineKeyboardMarkup()
start_markup_btn1 = types.InlineKeyboardButton(
    text="Да, конечно!", callback_data="начало")
start_markup.add(start_markup_btn1)

begin_markup = types.InlineKeyboardMarkup()
begin_markup_btn1 = types.InlineKeyboardButton(
    text="1 отряд", callback_data="1 отряд")
begin_markup_btn2 = types.InlineKeyboardButton(
    text="2 отряд", callback_data="2 отряд")
begin_markup_btn3 = types.InlineKeyboardButton(
    text="3 район", callback_data="3 отряд")
begin_markup_btn4 = types.InlineKeyboardButton(
    text="4 отряд", callback_data="4 отряд")
begin_markup_btn5 = types.InlineKeyboardButton(
    text="5 отряд", callback_data="5 отряд")
begin_markup_btn6 = types.InlineKeyboardButton(
    text="6 отряд", callback_data="6 отряд")
begin_markup.add(begin_markup_btn1,
                 begin_markup_btn2, begin_markup_btn3, begin_markup_btn4, begin_markup_btn5, begin_markup_btn6)

first_squad_markup = types.InlineKeyboardMarkup()
first_squad_markup_btn1 = types.InlineKeyboardButton(
    text="1. 1 ответ", callback_data="1 ответ")
first_squad_markup_btn2 = types.InlineKeyboardButton(
    text="2. 2 ответ", callback_data="2 ответ")
first_squad_markup_btn3 = types.InlineKeyboardButton(
    text="3. 2 ответ", callback_data="3 ответ")
first_squad_markup.add(first_squad_markup_btn1,
                       first_squad_markup_btn2, first_squad_markup_btn3)


back_first_markup = types.InlineKeyboardMarkup()
back_first_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться", callback_data="вернуться")
back_first_markup.add(back_first_markup_btn1)


four_sqaud_markup = types.InlineKeyboardMarkup()
four_sqaud_markup_btn1 = types.InlineKeyboardButton(
    text="Миссию принял", callback_data="операция рад")
four_sqaud_markup.add(four_sqaud_markup_btn1)
