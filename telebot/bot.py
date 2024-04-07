import telebot
from telebot import apihelper
from parsing import parsing
from os.path import exists

TOKEN = ""
proxies = {
    'http': '' ,
    'https': '',
}

apihelper.proxy = proxies

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'send "/help" for help\n'
                          'or text me')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'send /parsing for news from pythondigest.ru (about python)\n'
                          'send /file for data news\n'
                          'send "any text" for revers "txet yna"')



@bot.message_handler(commands=['parsing'])
def parse_site(message):
    chat_id = message.chat.id
    news = parsing()
    for new_s in news[:5]:
        bot.send_message(chat_id, f'{new_s[0]} - {new_s[1]}')


@bot.message_handler(commands=['file'])
def send_file(message):
    chat_id = message.chat.id
    if exists('data.csv'):
        with open('data.csv', 'r', encoding='utf8') as f:
            bot.send_document(chat_id, f)
    else:
        bot.send_message(chat_id, 'Файл не сформирован. Используйте команду /parsing для его формирования')


@bot.message_handler(content_types=['text'])
def reverse_text(message):
    text = message.text[::-1]
    bot.reply_to(message, text)


bot.polling()
