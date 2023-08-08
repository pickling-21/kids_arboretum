from secret import *
from telebot import types

privet = '''Только что закончилась зарядка, и сейчас перед нами уникальный выбор - продолжить нашу путешествие по тропе здоровья, сквозь различные испытания, и ощутить на себе перемену от пластиковой бутылки до дивана. Этот путь может приоткрыть дверь к невероятным возможностям и преобразить наше существование, если мы пойдем дальше.'''
privet_markup = types.InlineKeyboardMarkup(row_width=1)
privet_markup_btn1 = types.InlineKeyboardButton(
    text="Отлично! Я уже ощущаю себя бутылкой", callback_data="2 да")
privet_markup_btn2 = types.InlineKeyboardButton(
    text="Что то я не понял... Кто я?", callback_data="2 кто я")
privet_markup.add(privet_markup_btn1, privet_markup_btn2)


butilka = '''Как начинается жизнь пластиковой бутылки? Словно рождение нового дня, вы оказываетесь на производственной ленте. Каждая из вас, великолепные бутылки, уникальна и неповторима, как звезды на ночном небе.

Теперь представьте, как ваши ободранные боковины ощущают ласковое прикосновение рук человека, который наполняет вас жизненной энергией. Вы становитесь источником питания, даря глоток освежающей жидкости жаждущему человечеству.

О, но ваш путь далеко не ограничивается одним лишь использованием! Ваша удивительная природа предрекает новые горизонты. Когда ваш путь достигает конца, вы можете открыть для себя сокровище переработки.

И здесь начинается настоящее волшебство! Вас не забрасывают на помойку, вы оживаете в новом обличье. Вы снова готовы служить, только теперь уже в другом качестве - как часть нового изделия, воплощающего смысл устойчивости и бережного отношения к миру.

Путешествие пластиковой бутылки - это история перемен, возрождения и постоянного стремления к преображению. Друзья мои, позвольте себе почувствовать ее силу и магию в своей жизни. Будьте как пластиковая бутылка - готовы меняться, преображаться и продолжать свой уникальный путь, исследуя новые горизонты и оставаясь всегда полными жизни и энергии'''

butilka_markup = types.InlineKeyboardMarkup(row_width=1)
butilka_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, хорошо, я бутылка", callback_data="2 понял")
butilka_markup.add(butilka_markup_btn1)


sorting = 'Тогда сортируемся'
sorting_markup = types.InlineKeyboardMarkup(row_width=1)
sorting_markup_btn1 = types.InlineKeyboardButton(
    text="Я готов сортировать", callback_data="2 сортировка")
sorting_markup_btn2 = types.InlineKeyboardButton(
    text="Расскажи про сортировку мусора подробнее", callback_data="2 про сортировка")

sorting_markup.add(sorting_markup_btn1, sorting_markup_btn2)


about_sorting = '''Пластик - это удивительный материал, который используется повсюду. Но когда мы не заботимся о пластиковых отходах, они могут попадать в нашу природу и вредить ей. Поэтому мы должны научиться правильно обращаться с пластиком.

Когда у вас есть пластиковые бутылки, контейнеры или упаковка, не выбрасывайте их вместе с обычным мусором. Найдите специальные контейнеры для переработки пластика. Когда мы сортируем пластик, он отправляется на переработку, и из него делают новые вещи! Это означает, что мы помогаем природе и экономим ресурсы.

Кроме того, давайте учимся выбирать продукты с меньшим количеством пластика. Например, можно использовать переиспользуемые пластиковые бутылки или тканевые сумки вместо пластиковых пакетов. Таким образом, мы сокращаем количество пластика, которое попадает в окружающую среду.

Помните, что каждый из нас может стать экологическим героем, сортируя мусор и бережно обращаясь с пластиком. Давайте сделаем наш мир чище, светлее и заботливее! '''
about_sorting_markup = types.InlineKeyboardMarkup(row_width=1)
about_sorting_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, спасибо", callback_data="2 понял")
about_sorting_markup.add(about_sorting_markup_btn1)


sorting_ex = 'В какой контейнер это положить?'
sorting_ex_markup = types.InlineKeyboardMarkup(row_width=1)
sorting_ex_markup_btn1 = types.InlineKeyboardButton(
    text="пластиковый контейнер", callback_data="2.1t")
sorting_ex_markup_btn2 = types.InlineKeyboardButton(
    text="контейнер для стекла", callback_data="2.1f")
sorting_ex_markup_btn3 = types.InlineKeyboardButton(
    text="контейнер для бумаги", callback_data="2.2f")
sorting_ex_markup.add(sorting_ex_markup_btn1,
                      sorting_ex_markup_btn2, sorting_ex_markup_btn3)


def send_query(user, answer):
    if answer == "2 отряд":
        states[user] = "2"
        bot.send_message(
            user,  privet, reply_markup=privet_markup)

    if answer == "2 кто я":
        states[user] = "2 бутылка"
        bot.send_message(
            user,  butilka, reply_markup=butilka_markup)

    if answer == "2 понял" or answer == "2 да":
        states[user] = "2 он бутылка"
        bot.send_message(
            user,  sorting, reply_markup=sorting_markup)

    if answer == "2 про сортировка":
        bot.send_message(user,  about_sorting,
                         reply_markup=about_sorting_markup)
        states[user] = "2 он бутылка"

    if answer == "2 сортировка":
        bot.send_message(user,  sorting_ex, reply_markup=sorting_ex_markup)
