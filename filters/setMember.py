from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from database.connect import group_get_setting, usercount

class SetMember(BoundFilter):

    async def check(self, msg: types.Message):
        data = group_get_setting(msg.chat.id)[0]
        c = usercount(msg.from_user.id, msg.chat.id)
        if data[2] == 0: return False
        if int(data[2]) <= c:
            return False
        else: return True