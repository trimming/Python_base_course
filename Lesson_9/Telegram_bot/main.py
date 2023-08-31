import telebot
import json
import requests
from random import *

menu = []
order = []

API_TOKEN = '6515813236:AAG3l7cwuVUL8OCcaxgTiP5oKpNljFY2mpo'
bot = telebot.TeleBot(API_TOKEN)
API_URL = 'https://7012.deeppavlov.ai/model'

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
    bot.send_message(message.chat.id, 'Добрый день! Вас приветствует сервис предварительного заказа нашего ресторана.\n'
                     'Команды нашего сервиса:\n'
                     '/menu - показать меню;\n'
                     '/add - добавить блюдо в заказ;\n'
                     '/order - показать ваш заказ;\n'
                     '/save - сохранить и отправить заказ;\n'
                     '/help - нужна помощь;\n'
                     '/wiki <вопрос> - скоротать время;\n'
                     '/del + блюдо - удалить блюдо;\n'
                     '/stop - выйти из сервиса')
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

@bot.message_handler(commands=['add'])
def add_dish(message):
    bot.send_message(message.chat.id, 'Прошу ввести блюдо из меню:')
    bot.send_message(message.chat.id, ', '.join(menu))
    @bot.message_handler(content_types=['text'])
    def get_dish_name(message):
        if message.text in menu:
            order.append(message.text)
            bot.send_message(message.chat.id, 'Блюдо успешно добавлено в ваш заказ!\n'
                             'Что-нибудь еще?')
        else:
            bot.send_message(message.chat.id, 'К сожалению, такого блюда нет в сегодняшнем меню(')    

@bot.message_handler(commands=['help'])
def call_help(message):
    bot.send_message(message.chat.id, 'Официант уже идет к Вам!')

@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = ' '.join(quest)
    data = {'question_raw':[qq]}
    try:
        res =requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, 'Что-то я ничего не нашел :-(')     

@bot.message_handler(commands=['order'])             
def show_order(message):
    try:
        bot.send_message(message.chat.id, ', '.join(order))
        bot.send_message(message.chat.id, 'Все верно?\n')                
    except:
        bot.send_message(message.chat.id, 'Ваш заказ пуст.')    

@bot.message_handler(commands=['stop'])
def stop_bot(message):
    bot.send_message(message.chat.id, 'Сервис остановил работу. До новых встреч!')    

@bot.message_handler(commands=['del'])
def del_dish(message):    
    dish = message.text.split()[1:]
    dish_name = ' '.join(dish)
    if dish_name in order:
        order.remove(dish_name)
        bot.send_message(message.chat.id, 'Блюдо удалено.')
    else:
        bot.send_message(message.chat.id, 'Такого блюда нет в заказе.')                

bot.polling()