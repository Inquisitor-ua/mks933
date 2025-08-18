import telebot
TOKEN = '7732163290:AAGu2Iyjz98t-Nx4UJ71Z5RBB0z7DDTVVeU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'home'])
def start(message):
    bot.reply_to(message, "Привет! Я твой персональный помощник)")
    
@bot.message_handler(content_types=['text'])
def message_answer(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Привет, дружище! Рад видеть тебя")
    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id, "Все отлично! А у тебя как?")
    else:
        bot.send_message(message.chat.id, "Не понял тебя(")
    
bot.infinity_polling(skip_pending=True)