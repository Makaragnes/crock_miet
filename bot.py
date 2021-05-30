#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import telebot
from apiai import apiai

bot = telebot.TeleBot("Здесь был токен")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, могу ли я чем-то помочь?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    request = apiai.ApiAI('Здесь был токен, а сейчас его нет, плак плак').text_request()
    request.lang = 'ru'
    request.session_id = 'Gamification'
    request.query = message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = ''
    response = responseJson['result']['fulfillment']['speech']

    if response:
        response = response
    else:
        response = 'Не могли бы вы повторить ваш вопрос, я не до конца понял.'
    bot.send_message(response.chat.id, response.text)


if __name__ == '__main__':
    bot.infinity_polling()
