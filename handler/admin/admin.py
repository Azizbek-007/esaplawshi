from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from filters.private_chat import IsPrivate
from config.config import dp, admins
from keyboard.reply import admin_btn

@dp.message_handler(Command('admin'), IsPrivate(), user_id=admins)
async def start(message: types.Message):
    await message.answer("Welcome to admin panel", 'html', reply_markup=admin_btn())