import telebot
from bot_logic import help_bot
from bot_logic import gift_23
from bot_logic import gift_8

bot = telebot.TeleBot("7808813003:AAHwxaDYLW4NFEwu9tMo3o5TG8mgplO6gOY")


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')


@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, help_bot())


@bot.message_handler(commands=['gift23'])
def send_gift23(message):
    bot.reply_to(message, gift_23())


@bot.message_handler(commands=['gift8'])
def send_gift8(message):
    bot.reply_to(message, gift_8())

# Запуск бота
bot.polling()
