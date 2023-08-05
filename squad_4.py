from telebot import types

privet = "Привет, путник. Нам нужна твоя помощь. Отправляйся к большой красной рыбе, которая думает что она чайка, она все расскажет. И помни, что времени мало. Удачи."


prvet_markup = types.InlineKeyboardMarkup()
prvet_markup_btn1 = types.InlineKeyboardButton(
    text="Миссию принял", callback_data="операция рад")
prvet_markup.add(prvet_markup_btn1)

