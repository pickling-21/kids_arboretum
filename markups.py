from telebot import types

start_markup = types.InlineKeyboardMarkup()
start_markup_btn1 = types.InlineKeyboardButton(
    text="Да, конечно!", callback_data="правила")
start_markup.add(start_markup_btn1)

begin_markup = types.InlineKeyboardMarkup()
begin_markup_btn1 = types.InlineKeyboardButton(
    text="1 район", callback_data="1 отряд")
begin_markup_btn2 = types.InlineKeyboardButton(
    text="2 район", callback_data="2 отряд")
begin_markup_btn3 = types.InlineKeyboardButton(
    text="3 район", callback_data="3 отряд")
begin_markup_btn4 = types.InlineKeyboardButton(
    text="4 район", callback_data="4 отряд")
begin_markup_btn5 = types.InlineKeyboardButton(
    text="5 район", callback_data="5 отряд")
begin_markup_btn6 = types.InlineKeyboardButton(
    text="6 район", callback_data="6 отряд")
begin_markup.add(begin_markup_btn1,
                 begin_markup_btn2, begin_markup_btn3, begin_markup_btn4, begin_markup_btn5, begin_markup_btn6)

karta = 'https://imageup.ru/img18/4471053/raiony.jpg'


pravila = '''Правила:
1. Максимально включите воображение: Включайте свою фантазию на полную мощность! Создавайте уникальные решения, задания будут давать такую возможность.
2. Честное выполнение заданий: Пожалуйста, соблюдайте правило честности. Выполняйте задания так, как они заданы, без обмана или обхода правил.
3. Не берите, пожалуйста, инвентарь. Или возвращайте его на место. Хочется, чтобы после вас квест смогли проходить другие дети.
4. Соблюдение конфиденциальности: Если вам дается какая-либо информация или подсказка, которая предполагает конфиденциальность, не раскрывайте её другим участникам.
5. Главное — наслаждайтесь процессом! Квест создан для вашего развлечения и познавательного опыта, так что не забудьте повеселиться.
6. Осторожно! Были использованы нейросети! Поэтому если что-то покажется нелогичным или странным, то мы извиняемся. 

Понял правила?
'''

pravila_markup = types.InlineKeyboardMarkup()
pravila_markup_btn1 = types.InlineKeyboardButton(
    text="Да, конечно! Я ставлю электронную подпись под ними.", callback_data="начало")
pravila_markup.add(pravila_markup_btn1)

poryadok = '''Рекомендуймый порядок прохождения:
1 -> 3 -> 2 -> 4 -> 6 -> 5'''
