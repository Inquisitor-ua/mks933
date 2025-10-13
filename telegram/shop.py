import json
import telebot
import bs4
import requests
import parc_template
from telebot import types
TOKEN = "8492962669:AAGSr21A8htjmfV6nSHtpiwkxx5I8fOeZmw"
bot = telebot.TeleBot(TOKEN)

def make_markup(*args, one_time = False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time)
    for btn in args:
        item = types.KeyboardButton(btn)
        markup.add(item)
    return markup

def make_markup(*args, one_time = False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time)
    for btn in args:
        item = types.KeyboardButton(btn)
        markup.add(item)
    return markup

@bot.message_handler(commands=['start', 'home'])
def start(message):
    bot.reply_to(message, 'Ты в главном меню', reply_markup=make_markup('Посмотреть фильмы', "Мои заказы"))
    
@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Посмотреть фильмы':
        films = parc_template.get_random_films()
        answer = ''
        number = 1
        for film in films:
            answer += f"{number}. {film}\n"
            number += 1
        msg = bot.send_message(message.chat.id, answer, reply_markup=make_markup('Смотрим', "Меняй", one_time=True))
        bot.register_next_step_handler(msg, catalog)
    elif message.text == 'Мои заказы':
        ...
    else:
        bot.reply_to(message, 'Не понял тебя, возвращаю на главное меню', reply_markup=make_markup('Посмотреть фильмы', "Мои заказы"))

def catalog(message):
    # markup = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton('Купить', callback_data='Buy')
    # btn2 = types.InlineKeyboardButton('Отказаться', callback_data='Decline')
    # markup.add(btn1, btn2)
    if message.text == 'Смотрим':
        bot.send_message(message.chat.id, 'Приятного просмотра')
    elif message.text == 'Меняй':
        films = parc_template.get_random_films()
        answer = ''
        number = 1
        for film in films:
            answer += f"{number}. {film}\n"
            number += 1
        msg = bot.send_message(message.chat.id, answer, reply_markup=make_markup('Смотрим', "Меняй", one_time=True))
        bot.register_next_step_handler(msg, catalog)
    else:
        bot.send_message(message.chat.id, 'Не понял тебя, возвращаю в главное меню', reply_markup=make_markup('Посмотреть фильмы', "Мои заказы", one_time=True))


# @bot.callback_query_handler(func = lambda call: True)
# def callback_handle(call):
#     if call.data == 'Buy':
#         bot.answer_callback_query(call.id, 'Купили')
#         bot.send_message(call.message.chat.id, 'Вы купили')
#     elif call.data == 'Decline':
#         bot.answer_callback_query(call.id, 'Отказ')
#         bot.send_message(call.message.chat.id, 'Отказались')

if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)