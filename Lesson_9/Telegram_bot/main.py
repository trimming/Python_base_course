import telebot
import json
import requests
from random import *

menu = []
order = []

API_TOKEN = '6515813236:AAG3l7cwuVUL8OCcaxgTiP5oKpNljFY2mpo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    menu.append('Паста Карбонара')
    menu.append('Стейк из семги')
    menu.append('Каре ягненка')
    menu.append('Свиные медальоны')
    menu.append('Скрэмбл с зеленью')
    menu.append('Классический омлет')
    menu.append('Цезарь с курицей')
    menu.append('Салат из свежих овощей')
    menu.append('Морковный пирог')
    bot.send_message(message.chat.id, 'Добрый день! Вас приветствует сервис предварительного заказа нашего ресторана.')
@bot.message_handler(commands=['menu'])
def show_menu(message):
    try:
        bot.send_message(message.chat.id, 'Меню на сегодня:')
        bot.send_message(message.chat.id, ', '.join(menu))
    except:
        bot.send_message(message.chat.id, 'Извините, сегодня санитарный день.')
@bot.message_handler(commands=['save'])
def save_order(message):
    with open("order.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(order, ensure_ascii=False))
        bot.send_message(message.chat.id, "Ваш заказ был принят в работу")


bot.polling()