import telebot
import bot
import config


def memopediya(message):
    chat_id = message.chat.id
    text = message.text
    bot.send_photo(chat_id, config.url1)


