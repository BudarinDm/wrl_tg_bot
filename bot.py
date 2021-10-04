import telebot
import config
from api import firestore
from menu import markups

bot = telebot.TeleBot(config.TOKEN)

isActive = False


@bot.message_handler(commands=['start'])
def start_handler(message):
    global isActive
    if not isActive:
        chat_id = message.chat.id
        text = message.text
        bot.send_message(chat_id, 'Добро пожаловать прихожанин! Что ты хочешь?',
                         reply_markup=markups.source_markup)


@bot.message_handler(content_types='text')
def menu(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text == 'мемопедия':
        bot.send_photo(chat_id, config.url1)
    if text == 'календарь':
        bot.send_message(chat_id, 'Эта функция еще не реализована')
        # def
    if text == 'список прихожан':
        bot.send_message(chat_id, 'Эта функция еще не реализована')
        # def
    if text == 'профиль':
        bot.send_message(chat_id, 'Эта функция еще не реализована')
        # def
    if text == 'не знаешь что покурить?':
        bot.send_message(chat_id, 'Эта функция еще не реализована')
        # def
    if text == 'хотелки/предложения/замечания':
        bot.send_message(chat_id, 'Эта функция еще не реализована')
        # def


bot.infinity_polling()
