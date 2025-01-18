from datetime import time

import telebot

bot = telebot.TeleBot('7748218830:AAFmQoLjaKz3DGpg99oJKkw3qhXPLkqOhIY')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)




