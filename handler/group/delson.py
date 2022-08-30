from aiogram import types
from config.config import dp, bot
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import members_clear
from keyboard.Inline import shareebtn

@dp.message_handler(IsAdmin(), is_chat_admin=True, commands=['delson'])
async def delson(message: types.Message):
        await message.delete()
        members_clear(message.chat.id)
        me = await bot.get_me()
        text = lang.get('delson').format(message.chat.title)
        await message.answer(text, 'html', reply_markup=shareebtn(me.username))