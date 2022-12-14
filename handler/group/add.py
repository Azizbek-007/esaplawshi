from aiogram import types
from config.config import dp, bot
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import group_setting
from keyboard.Inline import shareebtn

@dp.message_handler(IsAdmin(), is_chat_admin=True, commands=['add'])
async def add_member_for_per(message: types.Message):
    await message.delete()
    me = await bot.get_me()
    if message.text == "/add off":
        group_setting(message.chat.id, 0)
        text = lang.get('tarif_off')
        await message.answer(text, 'html', reply_markup=shareebtn(me.username))
    try:
        son =int(message.text.split("/add ")[1])
        group_setting(message.chat.id, son)
        text = lang.get('instaled_tar').format(message.chat.title, son)
        await message.answer(son, 'html', reply_markup=shareebtn(me.username))
    except:
        text = lang.get('xadd')
        await message.answer(text, 'html', reply_markup=shareebtn(me.username))