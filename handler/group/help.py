from aiogram import types
from config.config import dp, bot 
from filters.bot_admin_chat import IsAdmin
from keyboard.Inline import start_btn
from lang.uz import lang

@dp.message_handler(IsAdmin(), commands=['help'])
async def help(message: types.Message):
        await message.delete()
        if message.from_user.is_bot == False:
            me = await bot.get_me()
            text = lang.get('help')
            await message.answer(text, reply_markup=start_btn(me.username))