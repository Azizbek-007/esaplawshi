from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from config.config import bot, bot_id

class IsAdmin(BoundFilter):

    async def check(self, call: types.CallbackQuery):
        get_chat = await bot.get_chat_member(call.message.chat.id, bot_id)
        if get_chat.status == 'administrator': return True