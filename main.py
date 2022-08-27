from aiogram import executor
import logging
from config.config import dp
from handler import message


logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True, allowed_updates=[
                'message', 
                'chat_member', 
                'my_chat_member', 
                'callback_query'
                ])