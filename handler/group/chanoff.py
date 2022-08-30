from aiogram import types
from config.config import dp
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import chan_off_on

@dp.message_handler(IsAdmin(), is_chat_admin=True, commands=['chanoff'])
async def chanoff(message: types.Message):
    await message.delete()
    chan_off_on(message.chat.id, 'off')
    await message.answer("off")