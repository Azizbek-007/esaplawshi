from aiogram import types
from filters.private_chat import IsPrivate
from config.config import dp, admins
from keyboard.reply import admin_btn
from aiogram.dispatcher import FSMContext
from database.connect import user_count, group_count

@dp.message_handler(IsPrivate(), text='Cancel', state='*', user_id=admins)
async def canceled(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("canceled", reply_markup=admin_btn())

@dp.message_handler(IsPrivate(), text='Statistika', state='*', user_id=admins)
async def Statistika(message: types.Message, state: FSMContext):
    usercount = user_count()[0][0]
    groupcount = group_count()[0][0]
    print(usercount, groupcount)
    await message.answer(
        f"statisika:\nusers: {usercount}\ngroups: {groupcount}",)