from aiogram import types
from config.config import dp, bot
from filters.bot_admin_chat import IsAdmin
from lang.uz import lang
from database.connect import tops

@dp.message_handler(IsAdmin(), is_chat_admin=True, commands=['top'])
async def top(message: types.Message):
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