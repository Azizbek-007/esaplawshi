from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from database.connect import usercount, group_get_setting

class OkMember(BoundFilter):

   async def check(self, call: types.CallbackQuery):
        Grcount = int(group_get_setting(call.message.chat.id)[0][2])
        c = int(usercount(call.from_user.id, call.message.chat.id))
        if Grcount == 0 or Grcount <= c: return True


class SetMember(BoundFilter):

    async def check(self, call: types.CallbackQuery):
        Grcount = int(group_get_setting(call.message.chat.id)[0][2])
        c = int(usercount(call.from_user.id, call.message.chat.id))
        if Grcount != 0 or Grcount > c: return True

