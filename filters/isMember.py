from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from config.config import bot

class IsMember(BoundFilter):

    async def check(self, message: types.Message):
        get_chat = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if get_chat.status in ['member', 'restricted']: return True

 