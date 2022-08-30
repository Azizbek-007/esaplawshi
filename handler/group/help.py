from aiogram import types
from config.config import dp, bot 
from filters.bot_admin_chat import IsAdmin
from keyboard.Inline import start_btn
from lang.uz import lang
from aiogram.dispatcher import FSMContext

@dp.message_handler(IsAdmin(), commands=['help'])
async def help(message: types.Message, state: FSMContext):
        await message.delete()
        user_data = await state.get_data()
        try: await bot.delete_message(message.chat.id, user_data['mid'])
        except: pass
        if message.from_user.is_bot == False:
            me = await bot.get_me()
            text = lang.get('help')
            a = await message.answer(text, reply_markup=start_btn(me.username))
            await state.update_data(mid=a.message_id)