from telebot import types

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Мемопедия')
source_markup_btn2 = types.KeyboardButton('Календарь')
source_markup_btn3 = types.KeyboardButton('Список прихожан')
source_markup_btn4 = types.KeyboardButton('Профиль')
source_markup_btn5 = types.KeyboardButton('Не знаешь что покурить?')
source_markup_btn6 = types.KeyboardButton('Хотелки/предложения/замечания')

source_markup.add(
    source_markup_btn1,
    source_markup_btn2,
    source_markup_btn3,
    source_markup_btn4,
    source_markup_btn5,
    source_markup_btn6)
