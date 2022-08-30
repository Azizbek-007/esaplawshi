from aiogram import types
from filters.private_chat import IsPrivate
from config.config import dp, admins
from keyboard.reply import cancel_btn
from state.send_message import for_send
from utils.send_message import send_message
import asyncio
from aiogram.dispatcher import FSMContext
from database.connect import groups_id, group_status_up

@dp.message_handler(IsPrivate(), text='Send Groups', user_id=admins)
async def send_users(message: types.Message):
    await for_send.permission_group.set()
    await message.answer("Send me a message:", reply_markup=cancel_btn())


@dp.message_handler(state=for_send.permission_group, content_types=types.ContentTypes.ANY, user_id=admins)
async def sending(message: types.Message, state: FSMContext):
    send, nosend = 0, 0
    await message.answer("Sending...")
    for u in groups_id():
        if await send_message(u[0], message):
            send += 1
        else:
            nosend += 1
            group_status_up(u[0])
        await asyncio.sleep(.05)
    await state.finish()
    await message.answer(f'Sended: {send}\nNosend: {nosend}')