from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
config = dotenv_values(".env")

API_TOKEN = config['BOT_TOKEN']
bot_id = API_TOKEN.split(':')[0]
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = [659692188, 1146006872]