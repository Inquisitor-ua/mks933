import telebot
TOKEN = "8492962669:AAGSr21A8htjmfV6nSHtpiwkxx5I8fOeZmw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "home"])
def start(message):
    bot.reply_to(message, "Hallo!")

@bot.message_handler(content_types=["text"])
def message_answer(message):
    if message.text == "Hallo":
        bot.send_message(message.chat.id, "Hallo Freund, wie gehts?")


bot.infinity_polling(skip_pending=True)