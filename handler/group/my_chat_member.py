from aiogram import types
from config.config import dp, bot, bot_id
from lang.uz import lang
from keyboard.Inline import shareebtn
from database.connect import reg_group

@dp.my_chat_member_handler()
async def group_in_bot_data(message: types.ChatMemberUpdated):
    try:
        if message.new_chat_member.status == 'administrator' and message.new_chat_member.can_delete_messages == True and int(message.new_chat_member.user.id) == int(bot_id):
            reg_group(message.chat.id)
            text = lang.get('bot_admin')
            await bot.send_message(message.chat.id, text, 'html')
            text = lang.get('bot_join')
            me = await bot.get_me()
            await bot.send_message(message.chat.id, text, reply_markup=shareebtn(me.username))
    except: pass

# @dp.message_handler(lambda msg: msg.text)
# async def Commands(message: types.Message):
#     text = lang.get('noadminbot').format(message.from_user.id, message.from_user.first_name)
#     await message.answer(text, 'html')