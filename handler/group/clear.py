from aiogram import types
from config.config import dp
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import member_clear

@dp.message_handler(IsAdmin(), is_chat_admin=True, is_reply=True, commands=['clean'])
async def clean(message: types.Message):
    await message.delete()
    member_clear(message.reply_to_message.from_user.id)
    await message.answer(lang.get('user_cl').format(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name), 'html')
