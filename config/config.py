from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
config = dotenv_values(".env")

API_TOKEN = '5471436970:AAEU53gM9p796eSkjPOZL9rhFgSZEF_qj4g'
bot_id = API_TOKEN.split(':')[0]
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = [5356014595, 1146006872]