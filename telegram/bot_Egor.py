import telebot
from telebot import types
TOKEN = '7732163290:AAGu2Iyjz98t-Nx4UJ71Z5RBB0z7DDTVVeU'

bot = telebot.TeleBot(TOKEN)

def make_markup(*args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for btn in args:
        item = types.KeyboardButton(btn)
        markup.add(item)
    return markup

@bot.message_handler(commands=['start', 'home'])
def start(message):
    bot.reply_to(message, "Привет! Я твой персональный помощник)", reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def message_answer(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет, дружище! Рад видеть тебя", reply_markup=make_markup('И я рад тебя видеть!'))
    elif message.text == 'Как дела?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton("Хорошо")
        item2 = types.KeyboardButton("Плохо")
        item3 = types.KeyboardButton("Не знаю")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Все отлично! А у тебя как?", reply_markup=markup)
    elif message.text  == 'Хорошо':
        bot.send_message(message.chat.id, "Вот и прекрасно")
    elif message.text  == 'Плохо':
        bot.send_message(message.chat.id, "Не грусти")
    else:
        bot.send_message(message.chat.id, "Не понял тебя(")

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Привет")
item2 = types.KeyboardButton("Как дела?")
markup.add(item1, item2)

bot.infinity_polling(skip_pending=True)