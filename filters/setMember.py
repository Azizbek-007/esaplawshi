from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from database.connect import group_get_setting, usercount

class SetMember(BoundFilter):

    async def check(self, msg: types.Message):
        try:
            data = int(group_get_setting(msg.chat.id)[0][2])
        except: 
            data = 0
        c = usercount(msg.from_user.id, msg.chat.id)
        if data == 0: return False
        if int(data) <= c:
            return False
        else: return True