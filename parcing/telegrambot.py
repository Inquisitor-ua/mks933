import telebot
TOKEN = "8492962669:AAGSr21A8htjmfV6nSHtpiwkxx5I8fOeZmw"

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=["start", "home"])
# def start(message):
#     bot.reply_to(message, "Hallo!")


@bot.message_handler(content_types=["text"])
def message_answer(message):
    if message.text == "Hallo":
        bot.send_message(message.chat.id, "Hallo Freund, wie gehts?")
    elif message.text == "Nicht gut":
        bot.send_message(message.chat.id, "Warum denn?")
    elif message.text == "Gut":
        bot.send_message(message.chat.id, "Das ist toll!")
    elif message.text == "Bye":
        bot.send_message(message.chat.id, "Auf wiedersehen!")
    elif message.text == "Guten Morgen":
        bot.send_message(message.chat.id,"Hi,was kann ich tun?")
    elif message.text == "Guten Tag":
        bot.send_message(message.chat.id, "Moinsen!!")
    elif message.text == "Guten Abend":
        bot.send_message(message.chat.id, "Abend 🤗")
    else:
        bot.send_message(message.chat.id, "Achso.")





bot.infinity_polling(skip_pending=True)