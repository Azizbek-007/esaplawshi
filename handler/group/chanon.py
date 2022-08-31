from aiogram import types
from config.config import dp, bot
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import chan_off_on
from keyboard.Inline import shareebtn


@dp.message_handler(IsAdmin(), is_chat_admin=True, commands=['chanon'])
async def chanoff(message: types.Message):
    await message.delete()
    chan_off_on(message.chat.id, 'on')
    text = lang.get('chanon')
    me = await bot.get_me()
    await message.answer(text, reply_markup=shareebtn(me.username))