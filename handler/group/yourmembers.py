from aiogram import types
from config.config import dp
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import usercount

@dp.message_handler(IsAdmin(), is_reply=True, commands=['yourmembers'])
async def yourmembers(message: types.Message):
    await message.delete()
    c = int(usercount(message.reply_to_message.from_user.id, message.chat.id))
    if c > 0:
        text = lang.get('ryes_add').format(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name, c)
        await message.answer(text, 'html')
    else:
        text = lang.get('rno_add').format(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)
        await message.answer(text, 'html')