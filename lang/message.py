import asyncio
import math
import time
from config.config import  dp, bot, bot_id
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat import IsPrivate

# languages
from lang.uz import lang

# Keyboards
from keyboard.Inline import start_btn, shareebtn, added_btn
from database.connect import reg_group, group_setting, group_get_setting, new_member, usercount, members_clear, member_clear, \
    tops, chan_off_on

async def isAdmin(msg)->bool:
    bot_data = await bot.get_chat_member(msg.chat.id, bot_id)
    if bot_data.status == 'administrator':
        return True

async def setMember(msg)->bool:
    data = group_get_setting(msg.chat.id)[0]
    c = usercount(msg.from_user.id, msg.chat.id)
    print(data[2])
    if int(data[2]) <= c:
        return True
    else: return False


















@dp.callback_query_handler(text = "member_added")
async def inline_with_check(call: types.CallbackQuery):
    print('keldi')
    if await isAdmin(call.message):
        data = await setMember(call.message)
        pr = await bot.get_chat(call.message.chat.id)
        new_permissions = types.ChatPermissions(pr.permissions,)
        print(new_permissions)
        await bot.restrict_chat_member(call.message.chat.id, call.from_user.id, 
                permissions=new_permissions)

