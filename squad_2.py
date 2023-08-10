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
    text="Погнали!", callback_data="2 сортировка")
sorting_markup_btn2 = types.InlineKeyboardButton(
    text="Расскажи про сортировку мусора подробнее", callback_data="2 про сортировка")

sorting_markup.add(sorting_markup_btn1, sorting_markup_btn2)


about_sorting = '''Пластик - это удивительный материал, который используется повсюду. Но когда мы не заботимся о пластиковых отходах, они могут попадать в нашу природу и вредить ей. Поэтому мы должны научиться правильно обращаться с пластиком.

Когда у вас есть пластиковые бутылки, контейнеры или упаковка, не выбрасывайте их вместе с обычным мусором. Найдите специальные контейнеры для переработки пластика. Когда мы сортируем пластик, он отправляется на переработку, и из него делают новые вещи! Это означает, что мы помогаем природе и экономим ресурсы.

Кроме того, давайте учится выбирать продукты с меньшим количеством пластика. Например, можно использовать многоразовые пластиковые бутылки или тканевые сумки вместо пластиковых пакетов. Таким образом, мы сокращаем количество пластика, которое попадает в окружающую среду.

Помните, что каждый из нас может стать экологическим героем, сортируя мусор и бережно обращаясь с пластиком. Давайте сделаем наш мир чище, светлее и заботливее! '''
about_sorting_markup = types.InlineKeyboardMarkup(row_width=1)
about_sorting_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, спасибо", callback_data="2 понял")
about_sorting_markup.add(about_sorting_markup_btn1)


sorting_ex = '_Какой контейнер мне выбрать?_'
# текст нашего сообщения

sorting_ex_markup = types.InlineKeyboardMarkup(row_width=1)
# cоздаем клавиатуру

sorting_ex_markup_btn1 = types.InlineKeyboardButton(
    text="пластиковый контейнер", callback_data="2.1t")
# создаем кнопку

sorting_ex_markup_btn2 = types.InlineKeyboardButton(
    text="контейнер для стекла", callback_data="2.1f")
sorting_ex_markup_btn3 = types.InlineKeyboardButton(
    text="контейнер для бумаги", callback_data="2.1f")


sorting_ex_markup.add(sorting_ex_markup_btn1,
                      sorting_ex_markup_btn2, sorting_ex_markup_btn3)
# совмещаем

prav = "Молодец, ты выбрала правильный вариант и ты сможешь продолжить свой путь до превращения в диван "
ne_prav = "Упс, ты выбрала неправильный контейнер, но не растраивайся подумай получше и продолжи свой путь до дивана."

prav_markup = types.InlineKeyboardMarkup(row_width=1)
prav_markup_btn1 = types.InlineKeyboardButton(
    text="Отлично идем дальше", callback_data="флекс")
prav_markup.add(prav_markup_btn1)

fleks_ex = '*Чтобы перейти на следующую стадию потанцуй (а если точнее пофлекси) и запиши видео со своим танцем. Только не дольше 15 секунд. Можешь прислать видеокружок. Как тебе удобней.*'


fleks = '_Вау, это была лютая туса. Мне говорили переработанные мусорки, что на этих вечеринках дико измельчает, но я не знала, что тут все именно так. Теперь я есть флекс._'
fleks_markup = types.InlineKeyboardMarkup(row_width=1)
fleks_markup_btn1 = types.InlineKeyboardButton(
    text="Узнать больше про эту стадию переработки", callback_data="серьезно флекс")
fleks_markup.add(fleks_markup_btn1)


fleks_ser = 'Сортированные пластиковые бутылки проходят через механическую обработку, которая включает их измельчение на мелкие частицы. Это может осуществляться с помощью специальных мельниц или грануляторов, которые превращают бутылки в мелкую дробь (флекс). На этом этапе можно остановится. Флекс уже является сырьем для новых продуктов.'
fleks_ser_markup = types.InlineKeyboardMarkup(row_width=1)
fleks_ser_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, идем дальше!", callback_data="баня ждем")
fleks_ser_markup.add(fleks_ser_markup_btn1)

banya_ex = '*Чтобы перейти на следующую стадию тебе нужно разогреться. Поэтому выйди на футбольное поле, на солнышко и сделай разминку.*'
banya_markup = types.InlineKeyboardMarkup(row_width=1)
banya_markup_btn1 = types.InlineKeyboardButton(
    text="Ух, как жарко! Я сделал разминку", callback_data="баня")
banya_markup.add(banya_markup_btn1)

banya = '''_Флекс - это не конечная стадия развития бутылки. Я разогрелась на футбольном поле, но этого мало, поэтому я решила пойти в баню, чтобы полежать на камнях. Меня разморило в бане и я стала вязко-текучей. Кто-то отрыл дверь, и меня сквозняком унесло на промышленный барабан на заводе, и я стала синтепоном._'''
banya_markup = types.InlineKeyboardMarkup(row_width=1)
banya_markup_btn1 = types.InlineKeyboardButton(
    text="Узнать больше про эту стадию переработки", callback_data="серьезно баня")
banya_markup.add(banya_markup_btn1)

banya_ser = ''' Полученные частички нагреваются до определенной температуры, при которой материал становится пластичным. Это позволяет легко формировать его в волокна или нити. После материал охлаждается и собирается в виде синтепона. '''
banya_ser_markup = types.InlineKeyboardMarkup(row_width=1)
banya_ser_markup_btn1 = types.InlineKeyboardButton(
    text="Хорошо, идем дальше!", callback_data="конец")
banya_ser_markup.add(banya_ser_markup_btn1)

end = '''_Потом мной набили диван. И именно так из бутылки я стала диваном._'''
end_markup = types.InlineKeyboardMarkup(row_width=1)
end_markup_btn1 = types.InlineKeyboardButton(
    text="Вернуться к выбору квеста", callback_data="вернуться")
end_markup.add(end_markup_btn1)


pictures = {
    1: 'https://imageup.ru/img271/4468490/kandinsky-download-1691315122299.jpg',
    2: 'https://imageup.ru/img285/4469257/kandinsky-download-1691593271100.png',
    3: 'https://imageup.ru/img227/4469280/kandinsky-download-1691314188522.jpg',
    4: 'https://imageup.ru/img135/4469254/kandinsky-download-1691592929214.jpg',
    5: 'https://imageup.ru/img194/4469275/kandinsky-download-1691596227374.png',
    6: 'https://imageup.ru/img254/4469306/kandinsky-download-1691314640289.jpg',
    7: 'https://imageup.ru/img204/4469268/kandinsky-download-1691594334996.png',
    8: 'https://imageup.ru/img221/4469271/kandinsky-download-1691595844531.png'
}

audio = 'https://cs3-12v4.vkuseraudio.net/s/v1/acmp/l_6viypIZIk5bpoOEfIk3KYyEhdssZOHUlzPXQEPoY6A9eHmME-ZQVBA8pXYvFpmVP1QVGvpOcZJgo739tL3w-MwMEnwysJaEdobQIPMlPdo5ofaWjEsQ8fbZ49tSVgWnyh79neAaXJsqgprquqZ6Fex_CHrFe1hQEfyTh9mBZgfiOxJUg.mp3?siren=1'


def send_video(user):
    if states[user] == '2 ждем видео':
        bot.send_message(user, fleks, reply_markup=fleks_markup,
                         parse_mode='Markdown')
        states[user] = 'флекс сделано'


def send_query(user, answer):
    if answer == "2 отряд":
        curr_squad = 2
        states[user] = "2"
        bot.send_photo(user, pictures[2])
        bot.send_message(
            user,  privet, reply_markup=privet_markup, parse_mode='Markdown')

    if answer == "2 кто я":
        states[user] = "2 бутылка"
        bot.send_photo(user, pictures[1])
        bot.send_message(
            user,  butilka, reply_markup=butilka_markup, parse_mode='Markdown')

    if answer == "2 понял" or answer == "2 да":
        states[user] = "2 он бутылка"
        bot.send_message(
            user,  sorting, reply_markup=sorting_markup, parse_mode='Markdown')

    if answer == "2 про сортировка":
        bot.send_photo(user, pictures[3])
        bot.send_message(user,  about_sorting,
                         reply_markup=about_sorting_markup, parse_mode='Markdown')
        states[user] = "2 он бутылка"

    if answer == "2 сортировка":
        bot.send_photo(user, pictures[4])
        bot.send_message(user,  sorting_ex,
                         reply_markup=sorting_ex_markup, parse_mode='Markdown')

    if answer == '2.1t':
        bot.send_message(user, prav, reply_markup=prav_markup,
                         parse_mode='Markdown')

    if answer == '2.1f':
        bot.send_message(user, ne_prav, parse_mode='Markdown')

    if answer == 'флекс':
        bot.send_photo(user, pictures[5])
        bot.send_message(user, fleks_ex,
                         parse_mode='Markdown')
        bot.send_audio(user, audio)
        states[user] = '2 ждем видео'

    if states[user] == 'флекс сделано':
        states[user] = '2 сделано'
        bot.send_message(user, fleks, reply_markup=fleks_markup,
                         parse_mode='Markdown')

    if answer == "серьезно флекс":
        bot.send_photo(user, pictures[6])
        bot.send_message(
            user, fleks_ser, reply_markup=fleks_ser_markup, parse_mode='Markdown')
    if answer == 'баня ждем':
        bot.send_photo(user, pictures[7])
        bot.send_message(
            user, banya_ex, reply_markup=banya_markup, parse_mode='Markdown')

    if answer == 'баня':
        bot.send_message(user, banya, reply_markup=banya_markup,
                         parse_mode='Markdown')

    if answer == 'серьезно баня':
        bot.send_message(
            user, banya_ser, reply_markup=banya_ser_markup, parse_mode='Markdown')

    if answer == 'конец':
        bot.send_photo(user, pictures[8])
        bot.send_message(user, end, reply_markup=end_markup,
                         parse_mode='Markdown')

    if answer == 'вернуться':
        states[user] = 0
