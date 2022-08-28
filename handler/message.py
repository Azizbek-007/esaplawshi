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
from database.connect import register_user, reg_group, group_setting, group_get_setting, new_member, usercount, members_clear, member_clear, \
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


@dp.message_handler(CommandStart(), IsPrivate())
async def start(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username 
    user = message.from_user.id
    register_user(user, username, first_name, last_name)
    text = lang.get('start').format(first_name)
    me = await bot.get_me()
    await message.answer(text, 'html', reply_markup=start_btn(me.username))

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        if message.from_user.is_bot == False:
            me = await bot.get_me()
            text = lang.get('help')
            await message.answer(text, reply_markup=start_btn(me.username))

@dp.message_handler(commands=['mymembers'])
async def mymembers(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        c = int(usercount(message.from_user.id, message.chat.id))
        if c > 0:
            text = lang.get('yes_add').format(message.from_user.id, message.from_user.first_name, c)
            await message.answer(text, 'html')
        else:
            text = lang.get('no_add').format(message.from_user.id, message.from_user.first_name)
            await message.answer(text, 'html')

@dp.message_handler(is_reply=True, commands=['yourmembers'])
async def yourmembers(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        c = int(usercount(message.reply_to_message.from_user.id, message.chat.id))
        if c > 0:
            text = lang.get('ryes_add').format(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name, c)
            await message.answer(text, 'html')
        else:
            text = lang.get('rno_add').format(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)
            await message.answer(text, 'html')

@dp.message_handler(is_chat_admin=True, commands=['top'])
async def top(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        data = tops(message.from_user.id, message.chat.id)
        if len(data) > 0:
            txt, i = "", 1
            for x in data:
                userdata = await bot.get_chat_member(message.chat.id, x[1])
                txt +=f"\n<b>{i}.</b> <a href='tg://user?id={x[1]}'>{userdata.user.first_name}</a>-{x[0]}"
            text = lang.get('top').format(message.chat.title, txt)
            i = i + 1
            await message.answer(text, 'html')
        else:
            text = "Guruhda hali top yoq:("
            await  message.answer(text)

@dp.message_handler(is_chat_admin=True, commands=['chanoff'])
async def chanoff(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        chan_off_on(message.chat.id, 'off')
        await message.answer("off")

@dp.message_handler(is_chat_admin=True, commands=['chanon'])
async def chanoff(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        chan_off_on(message.chat.id, 'on')
        await message.answer("on")


@dp.message_handler(is_chat_admin=True, commands=['delson'])
async def delson(message: types.Message):
     if await isAdmin(message):
        await message.delete()
        members_clear(message.chat.id)
        me = await bot.get_me()
        text = lang.get('delson').format(message.chat.title)
        await message.answer(text, 'html', reply_markup=shareebtn(me.username))

@dp.message_handler(is_chat_admin=True, is_reply=True, commands=['clean'])
async def clean(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        member_clear(message.reply_to_message.from_user.id)
        await message.answer(lang.get('user_cl').format(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name), 'html')

@dp.message_handler(is_chat_admin=True, commands=['add'])
async def add_member_for_per(message: types.Message):
    if await isAdmin(message):
        await message.delete()
        if message.text == "/add off":
            group_setting(message.chat.id, 0)
            text = lang.get('tarif_off')
            await message.answer(text, 'html')
            return
        try:
            son =int(message.text.split("/add ")[1])
            group_setting(message.chat.id, son)
            await message.answer(son)
        except ValueError:
            text = lang.get('xadd')
            await message.answer(text, 'html')

@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def logika(message: types.Message):
    reg_group(message.chat.id)
    try:
        if await isAdmin(message) == True:
            await message.delete()
            for x in message.new_chat_members:
                if x.is_bot == False and x.id != message.from_user.id:
                    new_member(message.from_user.id, x.id, message.chat.id)
    except: pass



@dp.my_chat_member_handler()
async def group_in_bot_data(message: types.ChatMemberUpdated):
    try:
        if message.new_chat_member.status == 'administrator' and message.new_chat_member.can_delete_messages == True and int(message.new_chat_member.user.id) == int(bot_id):
            text = lang.get('bot_admin')
            await bot.send_message(message.chat.id, text, 'html')
            text = lang.get('bot_join')
            me = await bot.get_me()
            await bot.send_message(message.chat.id, text, reply_markup=shareebtn(me.username))
    except: pass

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

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def restrict_chat_member_coun(message: types.Message):
    dataGr = group_get_setting(message.chat.id)[0]
    print('keldiddd')
    if dataGr[3] == "on":
        if message.from_user.is_bot:
            await message.delete()

    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    print(user.status)
    if await isAdmin(message) and user.status == 'restricted' or user.status == 'member':
        data = await setMember(message)
        if data != True: 
            await message.delete()
            number = int(dataGr[2])-int(usercount(message.from_user.id, message.chat.id))
            text = lang.get('adam_qos').format(message.from_user.id, message.from_user.first_name, f"{number}")
            a = await bot.send_message(message.chat.id, text, 'html', reply_markup=added_btn())
            await bot.restrict_chat_member(message.chat.id, message.from_user.id,
                                        until_date=math.floor(time.time()) + 5*60,
                                        permissions=types.ChatPermissions(can_send_messages=False, can_invite_users=True))
            await asyncio.sleep(300)
            await a.delete()
