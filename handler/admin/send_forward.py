from aiogram import types
from filters.private_chat import IsPrivate
from config.config import dp, admins
from keyboard.reply import cancel_btn
from state.send_message import for_send
from utils.send_message import send_message
import asyncio
from aiogram.dispatcher import FSMContext
from database.connect import groups_id, users_id, group_status_up, user_status_up

@dp.message_handler(IsPrivate(), text='Send Forward Groups', user_id=admins)
async def send_usersF(message: types.Message):
    await for_send.permission_send_forward.set()
    await message.answer("Send me a message:", reply_markup=cancel_btn())


@dp.message_handler(state=for_send.permission_send_forward, content_types=types.ContentTypes.ANY, user_id=admins)
async def sendingF(message: types.Message, state: FSMContext):
    send, nosend = 0, 0
    await message.answer("Sending...")
    for u in groups_id():
        try: 
            await message.forward(u[0])
            send += 1
        except:
            nosend += 1
            group_status_up(u[0])
        await asyncio.sleep(.05)
    await state.finish()
    await message.answer(f'Sended: {send}\nNosend: {nosend}')

@dp.message_handler(IsPrivate(), text='Send Forward User', user_id=admins)
async def send_usersU(message: types.Message):
    await for_send.permission_send_forward_user.set()
    await message.answer("Send me a message:", reply_markup=cancel_btn())


@dp.message_handler(state=for_send.permission_send_forward_user, content_types=types.ContentTypes.ANY, user_id=admins)
async def sendingU(message: types.Message, state: FSMContext):
    send, nosend = 0, 0
    await message.answer("Sending...")
    for u in users_id():
        try: 
            await message.forward(u[0])
            send += 1
        except:
            nosend += 1
            user_status_up(u[0])
        await asyncio.sleep(.05)
    await state.finish()
    await message.answer(f'Sended: {send}\nNosend: {nosend}')