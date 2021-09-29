import telebot
import config
import markups

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Добро пожаловать прихожанин! Что ты хочешь?', reply_markup=markups.source_markup)


@bot.message_handler(content_types='text')
def reg(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text == 'зарегестрироваться':
        bot.send_message(chat_id, 'Открыта страница зарегестрироваться')
    if text == 'календарь':
        bot.send_message(chat_id, 'Открыта страница календарь')
    if text == 'профиль':
        bot.send_message(chat_id, 'Открыта страница профиль')
    if text == 'миксы':
        bot.send_message(chat_id, 'Открыта страница регистрации')


bot.polling()
