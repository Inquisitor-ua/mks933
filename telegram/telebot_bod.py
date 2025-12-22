import telebot
import sqlite3
from telebot import types
TOKEN = "8532549204:AAHFEjAazVdNqn13RRSCtEP-acuuvhiNBH8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "home"])
def start(message):
    msg = bot.reply_to(message, "Hallo! Gib deinen Namen an: ")
    bot.register_next_step_handler(msg, enter_name)
    

@bot.message_handler(content_types=["text"])
def message_answer(message):
    ...

def enter_name(message):
    global name
    name = message.text
    msg = bot.reply_to(message, "Danke! Gib jetzt deinen Nachnamen an: ")
    bot.register_next_step_handler(msg, enter_lastname)
def enter_lastname(message):
    global lastname
    lastname = message.text
    db = sqlite3.connect("db.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, lastname, telegram_id) VALUES (?, ?, ?)", (name, lastname, message.chat.id))
    db.commit()
    db.close()


    
bot.infinity_polling(skip_pending=True)