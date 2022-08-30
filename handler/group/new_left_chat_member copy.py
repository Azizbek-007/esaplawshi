from aiogram import types
from config.config import dp
from filters.bot_admin_chat import IsAdmin
from database.connect import reg_group, new_member

@dp.message_handler(IsAdmin(), content_types=['new_chat_members', 'left_chat_member'])
async def logika(message: types.Message):
    reg_group(message.chat.id)
    try:
        await message.delete()
        for x in message.new_chat_members:
            if x.is_bot == False and x.id != message.from_user.id:
                new_member(message.from_user.id, x.id, message.chat.id)
    except: pass
