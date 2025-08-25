import telebot
from telebot import types
TOKEN = "8492962669:AAGSr21A8htjmfV6nSHtpiwkxx5I8fOeZmw"

bot = telebot.TeleBot(TOKEN)

def make_markup(*args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in args:
        item = types.KeyboardButton(btn)
        markup.add(item)
        return markup

@bot.message_handler(commands=["start", "home"])
def start(message):
    bot.reply_to(message, "Hallo!", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def message_answer(message):
    if message.text == "Hallo":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Gut")
        item2 = types.KeyboardButton("Schlecht")
        item3 = types.KeyboardButton("Tschüss")
        markup.add(item1, item2, item3)    
        bot.send_message(message.chat.id, "Hallo Freund, wie gehts?", reply_markup=markup)
    elif message.text == "Schlecht":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Egal")
        item2 = types.KeyboardButton("Tschüss")
        markup.add(item1, item2)    
        bot.send_message(message.chat.id, "Warum denn?", reply_markup=markup)
    elif message.text == "Gut":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Ja!")
        item2 = types.KeyboardButton("Tschüss")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Das ist toll!", reply_markup=markup)
    elif message.text == "Ja!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Tschüss")
        markup.add(item1)
        bot.send_message(message.chat.id, "Langweilig. Tschüss!", reply_markup=markup)
    elif message.text == "Egal":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Es ist jetzt egal. Tschüss!")
        item2 = types.KeyboardButton("Tschüss")
        markup.add(item1, item2)
        bot.send_message(message.chat.id,"Warum?", reply_markup=markup)
    elif message.text == "Es ist jetzt egal. Tschüss!Guten Tag":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Tschüss")
        markup.add(item2)
        bot.send_message(message.chat.id, "Ok, Bye!", reply_markup=markup)
    elif message.text == "Guten Abend":
        bot.send_message(message.chat.id, "Abend 🤗")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Hallo")
        item2 = types.KeyboardButton("Tschüss")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Achso.", reply_markup=markup)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Hallo")
item2 = types.KeyboardButton("Tschüss")
markup.add(item1, item2)



bot.infinity_polling(skip_pending=True)