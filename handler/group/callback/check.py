from aiogram import types
from config.config import dp, API_TOKEN, bot
from filters.callback.bot_admin_chat import IsAdmin
from filters.callback.setMember import SetMember, OkMember
from lang.uz import lang
from database.connect import botPr, cnumber

@dp.callback_query_handler(IsAdmin(), OkMember(), text='member_added')
async def check(call: types.CallbackQuery):
    pr = botPr(call.message.chat.id, API_TOKEN)
    new_permissions = types.ChatPermissions(**pr)
    await call.message.delete()
    await bot.restrict_chat_member(call.message.chat.id, call.from_user.id, 
                    permissions=new_permissions)
    
@dp.callback_query_handler(IsAdmin(), SetMember(), text='member_added')
async def check(call: types.CallbackQuery):
    c = cnumber(call.message.chat.id, call.from_user.id)
    text = lang.get('btnn').format(c)
    await call.answer(text, True)

