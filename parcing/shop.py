import telebot
from telebot import types
TOKEN = "8492962669:AAGSr21A8htjmfV6nSHtpiwkxx5I8fOeZmw"

bot = telebot.TeleBot(TOKEN)

def make_markup(*args):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in args:
        item = types.KeyboardButton(btn)                              ⚠️Lambda⚠️
        markup.add(item)
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hallo!", reply_markup=make_markup("Handy kaufen", "Meine Bestellungen"))


@bot.message_handler(content_types=["text"])
def message_answer(message):
    if message.text == "Handy kaufen":
        msg = bot.send_message(message.chat.id, "Deine Auswahl: ⬇️", reply_markup=make_markup("iPhone 17", "samsungGalaxy S24+", "Huawei 9", "Zurück"))
        bot.register_next_step_handler(msg, katalog)
    elif message.text == "Meine Bestellungen":
        msg = bot.send_message(message.chat.id, "...", reply_markup=make_markup())
    else:
        bot.send_message(message.chat.id, "Entschuldigung, ich habe dich nicht verstanden. Zurück zum Main menu.", reply_markup=make_markup("Handy kaufen", "Meine Bestellungen"))


def katalog(message):
    global phone
    phone = 'None'
    if message.text == "iPhone 17":
        phone = 'iPhone 17'
        msg = bot.send_message(message.chat.id, "iPhone 17 kaufen. Preis $1000", reply_markup=make_markup("Kaufen", "Zurück"))
        bot.register_next_step_handler(msg, bestätigung)
    elif message.text == "samsungGalaxy S24+":
        phone = "samsungGalaxy S24+"
        msg = bot.send_message(message.chat.id, "samsungGalaxy S24+ kaufen. Preis $799", reply_markup=make_markup("Kaufen", "Zurück"))
        bot.register_next_step_handler(msg, bestätigung)
    elif message.text == "Huawei 9":
        phone = "Huawei 9"
        msg = bot.send_message(message.chat.id, "Huawei 9. Preis $699", reply_markup=make_markup("Kaufen", "Zurück"))
        bot.register_next_step_handler(msg, bestätigung)
    elif message.text == "Zurück":
        msg = bot.send_message(message.chat.id, "Zurück zum Main menu.", reply_markup=make_markup("Handy kaufen", "Meine Bestellungen"))
        bot.register_next_step_handler(msg, message_answer)


def bestätigung(message):
    if message.text == "Kaufen":
        bot.send_message(message.chat.id, f"Sie haben ein {phone} gekauft!!", reply_markup=make_markup("Handy kaufen", "Meine Bestellungen"))
    elif message.text == "Zurück":
        msg = bot.send_message(message.chat.id, "Zurück", reply_markup=make_markup("iPhone 17", "samsungGalaxy S24+", "Huawei 9", "Zurück"))
        bot.register_next_step_handler(msg, katalog)


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)

