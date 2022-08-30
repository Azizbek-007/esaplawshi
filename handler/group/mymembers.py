from aiogram import types
from config.config import dp
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import usercount 

@dp.message_handler(IsAdmin(), commands=['mymembers'])
async def mymembers(message: types.Message):
    await message.delete()
    c = int(usercount(message.from_user.id, message.chat.id))
    if c > 0:
        text = lang.get('yes_add').format(message.from_user.id, message.from_user.first_name, c)
        await message.answer(text, 'html')
    else:
        text = lang.get('no_add').format(message.from_user.id, message.from_user.first_name)
        await message.answer(text, 'html')