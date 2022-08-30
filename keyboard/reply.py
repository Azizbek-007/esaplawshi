from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def admin_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Send Users'), KeyboardButton('Send Groups'))
    markup.add(KeyboardButton('Update'), KeyboardButton('Statistika'))
    return markup

def cancel_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Cancel'))
    return markup