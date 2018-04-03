# -*- coding: utf-8 -*-

import config
import telebot

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.reply_to(message, "/getId - получить Id своего аккаунта")

@bot.message_handler(commands = ["getId"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, 'your Id:' + str(message.chat.id))

if __name__ == '__main__':
    bot.polling(none_stop=True)