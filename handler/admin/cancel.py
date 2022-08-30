from aiogram import types
from filters.private_chat import IsPrivate
from config.config import dp, admins
from keyboard.reply import admin_btn
from aiogram.dispatcher import FSMContext

@dp.message_handler(IsPrivate(), text='Cancel', user_id=admins)
async def canceled(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("canceled", reply_markup=admin_btn())
