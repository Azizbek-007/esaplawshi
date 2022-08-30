from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_btn(bot_user):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("📢 BIZNING KANAL", 'https://t.me/')
    btn2 = InlineKeyboardButton("➕GURUHGA QO'SHISH➕", f"https://t.me/{bot_user}?startgroup=new")
    markup.add(btn)
    markup.add(btn2)
    return markup 

def shareebtn(bot_user):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("➕GURUHGA QO'SHISH➕", f"https://t.me/{bot_user}?startgroup=new")
    markup.add(btn)
    return markup  

def added_btn(user_id):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("✅ Odam qo'shdim", callback_data=f'member_added={user_id}')
    return markup.add(btn) 