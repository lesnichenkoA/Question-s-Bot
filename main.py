import telebot

from config import token
from database import insert_varible_into_table
from User import User

bot = telebot.TeleBot(token)
user_dict = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введите своё имя!')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    name = message.text

    user = User(name)
    user_dict[message.chat.id] = user

    bot.send_message(message.chat.id, f'Ваше имя: {name}\n\nВведите номер телефона!')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    number = message.text

    user = user_dict[message.chat.id]
    user.number = number

    bot.send_message(message.chat.id, f'Ваш номер телефона: {number}\n\nВведите email!')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    email = message.text

    user = user_dict[message.chat.id]
    user.email = email

    bot.send_message(message.chat.id, f'Ваш email: {email}\n\nВведите адрес!')
    bot.register_next_step_handler(message, get_address)


def get_address(message):
    address = message.text

    user = user_dict[message.chat.id]
    user.address = address

    name = user.name
    number = user.number
    email = user.email
    address = user.address

    bot.send_message(message.chat.id, f'Ваше имя: {name}\n\n'
                                      f'Ваш телефон: {number}\n\n'
                                      f'Ваш email: {email}\n\n'
                                      f'Ваш адрес: {address}')

    insert_varible_into_table(name, number, email, address)


bot.polling()
