from aiogram import types
from config.config import dp
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import group_setting

@dp.message_handler(IsAdmin(), is_chat_admin=True, commands=['add'])
async def add_member_for_per(message: types.Message):
    await message.delete()
    if message.text == "/add off":
        group_setting(message.chat.id, 0)
        text = lang.get('tarif_off')
        await message.answer(text, 'html')
        return
    try:
        son =int(message.text.split("/add ")[1])
        group_setting(message.chat.id, son)
        text = lang.get('instaled_tar').format(message.chat.title, son)
        await message.answer(son, 'html')
    except ValueError:
        text = lang.get('xadd')
        await message.answer(text, 'html')