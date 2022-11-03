from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def admin_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Send Users'), KeyboardButton('Send Groups'))
    markup.add(KeyboardButton('Send Forward User'), KeyboardButton('Send Forward Groups'))
    markup.add(KeyboardButton('Statistika'))
    return markup

def cancel_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Cancel'))
    return markup