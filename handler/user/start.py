from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat import IsPrivate
from config.config import dp, bot
from keyboard.Inline import start_btn
from database.connect import register_user
from lang.uz import  lang

@dp.message_handler(CommandStart(), IsPrivate())
async def start(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username 
    user = message.from_user.id
    register_user(user, username, first_name, last_name)
    text = lang.get('start').format(first_name)
    me = await bot.get_me()
    await message.answer(text, 'html', reply_markup=start_btn(me.username))