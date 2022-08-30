from aiogram import types
from config.config import dp, bot
from filters.bot_admin_chat import IsAdmin
from filters.setMember import SetMember
from lang.uz import lang
from database.connect import group_get_setting, usercount
from keyboard.Inline import  added_btn
import math
import asyncio
import time

@dp.message_handler(IsAdmin(), SetMember(), content_types=types.ContentTypes.ANY)
async def restrict_chat_member_coun(message: types.Message):
    dataGr = group_get_setting(message.chat.id)[0]
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status == 'restricted' or user.status == 'member':
        await message.delete()
        number = int(dataGr[2])-int(usercount(message.from_user.id, message.chat.id))
        text = lang.get('adam_qos').format(message.from_user.id, message.from_user.first_name, f"{number}")
        a = await bot.send_message(message.chat.id, text, 'html', reply_markup=added_btn())
        await bot.restrict_chat_member(message.chat.id, message.from_user.id,
                                    until_date=math.floor(time.time()) + 5*60,
                                    permissions=types.ChatPermissions(can_send_messages=False, can_invite_users=True))
        await asyncio.sleep(300)
        await a.delete()

@dp.message_handler(IsAdmin(), content_types=types.ContentTypes.ANY)
async def chan_on_off(message: types.Message):
    dataGr = group_get_setting(message.chat.id)[0]
    if dataGr[3] == "on":
        if message.from_user.is_bot:
            await message.delete()
