import time
import telebot

from func_db import add_user, create_table

bot = telebot.TeleBot('7748218830:AAFmQoLjaKz3DGpg99oJKkw3qhXPLkqOhIY')

@bot.message_handler(commands=['start'])
def start_message(message):
    add_user(message.from_user.id, message.from_user.username)
    bot.send_message(message.chat.id, ('Привет, ты написал мне /start'))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    log_message(message.from_user.id, message.text)
    bot.send_message(message.chat.id, ('Ваще, ты написал мне /start'))

while True:
    try:
        create_table()
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)







