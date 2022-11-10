from aiogram import types
from config.config import dp, bot
from filters.bot_admin_chat import IsAdmin
from filters.isMember import IsMember
from filters.setMember import SetMember
from lang.uz import lang
from database.connect import group_get_setting, usercount
from keyboard.Inline import  added_btn, shareebtn
from aiogram.dispatcher import FSMContext
import math
import asyncio
import time


@dp.message_handler(IsAdmin(), SetMember(), content_types=types.ContentTypes.ANY)
async def restrict_chat_member_coun(message: types.Message):
    try:
        dataGr = group_get_setting(message.chat.id)[0]
        print(dataGr[3])
        if dataGr[3] == "off":
            if message.sender_chat:
                await message.delete()
        dataGr = group_get_setting(message.chat.id)[0]
        user = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if user.status == 'restricted' or user.status == 'member':
            await message.delete()
            number = int(dataGr[2])-int(usercount(message.from_user.id, message.chat.id))
            text = lang.get('adam_qos').format(message.from_user.id, message.from_user.first_name, f"{number}")
            a = await bot.send_message(message.chat.id, text, 'html', reply_markup=added_btn(message.from_user.id))
            await bot.restrict_chat_member(message.chat.id, message.from_user.id,
                                        until_date=math.floor(time.time()) + 5*60,
                                        permissions=types.ChatPermissions(can_send_messages=False, can_invite_users=True))
            await asyncio.sleep(300)
            await a.delete()
    except: pass



@dp.message_handler(IsAdmin(), IsMember(), content_types=types.ContentTypes.ANY)
async def chan_on_off(message: types.Message, state: FSMContext):
    me = await bot.get_me()
    text = lang.get('rek_no').format(message.from_user.id, message.from_user.first_name)
    for entity in message.entities:
        if entity.type in ["url", "text_link", "mention"]:
            user_data = await state.get_data()
            try: await bot.delete_message(message.chat.id, user_data['mid'])
            except: pass
            await bot.delete_message(message.chat.id, message.message_id)
            a = await message.answer(text, 'html', reply_markup=shareebtn(me.username))
            return await state.update_data(mid=a.message_id)

    for entity in message.caption_entities:
        if entity.type in ["url", "text_link", "mention"]:
            user_data = await state.get_data()
            try: await bot.delete_message(message.chat.id, user_data['mid'])
            except: pass
            await bot.delete_message(message.chat.id, message.message_id)
            a = await message.answer(text, 'html', reply_markup=shareebtn(me.username))
            return await state.update_data(mid=a.message_id)
            
@dp.throttled(rate=1)
@dp.edited_message_handler(IsAdmin(), IsMember())
async def msg_handler(message: types.Message, state: FSMContext):
    text = lang.get('rek_no').format(message.from_user.id, message.from_user.first_name)
    me = await bot.get_me()
    for entity in message.entities:
        if entity.type in ["url", "text_link", "mention"]:
            user_data = await state.get_data()
            try: await bot.delete_message(message.chat.id, user_data['mid'])
            except: pass
            await bot.delete_message(message.chat.id, message.message_id)
            a = await message.answer(text, 'html', reply_markup=shareebtn(me.username))
            return await state.update_data(mid=a.message_id)

    for entity in message.caption_entities:
        if entity.type in ["url", "text_link", "mention"]:
            user_data = await state.get_data()
            try: await bot.delete_message(message.chat.id, user_data['mid'])
            except: pass
            await bot.delete_message(message.chat.id, message.message_id)
            a = await message.answer(text, 'html', reply_markup=shareebtn(me.username))
            return await state.update_data(mid=a.message_id)