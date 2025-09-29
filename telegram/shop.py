import telebot
from telebot import types
TOKEN = "7732163290:AAGu2Iyjz98t-Nx4UJ71Z5RBB0z7DDTVVeU"
bot = telebot.TeleBot(TOKEN)

def make_markup(*args, one_time = False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time)
    for btn in args:
        item = types.KeyboardButton(btn)
        markup.add(item)
    return markup

@bot.message_handler(commands=['start', 'home'])
def start(message):
    bot.reply_to(message, 'Ты в главном меню', reply_markup=make_markup('Купить телефон', "Мои заказы"))
    
@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Купить телефон':
        msg = bot.send_message(message.chat.id, 'Каталог:\n1. Iphone 17\n2. Pixel 9\n3. Samsung S25', reply_markup=make_markup('Iphone 17', "Pixel 9", 'Samsung S25', one_time=True))
        bot.register_next_step_handler(msg, catalog)
    elif message.text == 'Мои заказы':
        ...
    else:
        bot.reply_to(message, 'Не понял тебя, возвращаю на главное меню', reply_markup=make_markup('Купить телефон', "Мои заказы"))

def catalog(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Купить', callback_data='Buy')
    btn2 = types.InlineKeyboardButton('Отказаться', callback_data='Decline')
    markup.add(btn1, btn2)
    if message.text == 'Iphone 17':
        bot.send_message(message.chat.id, 'Iphone 17 стоит 1000$', reply_markup=markup)
    elif message.text == 'Pixel 9':
        bot.send_message(message.chat.id, 'Iphone 17 стоит 1000$', reply_markup=markup)
    elif message.text == 'Samsung S25':
        bot.send_message(message.chat.id, 'Iphone 17 стоит 1000$', reply_markup=markup)
    else:
        msg = bot.send_message(message.chat.id, 'Не понял тебя, возвращаю на каталог:\n\nКаталог:\n1. Iphone 17\n2. Pixel 9\n3. Samsung S25', reply_markup=make_markup('Iphone 17', "Pixel 9", 'Samsung S25', one_time=True))
        bot.register_next_step_handler(msg, catalog)

@bot.callback_query_handler(func = lambda call: True)
def callback_handle(call):
    if call.data == 'Buy':
        bot.answer_callback_query(call.id, 'Купили')
        bot.send_message(call.message.chat.id, 'Вы купили')
    elif call.data == 'Decline':
        bot.answer_callback_query(call.id, 'Отказ')
        bot.send_message(call.message.chat.id, 'Отказались')

if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)