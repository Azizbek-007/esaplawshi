from utils.commonds import set_default_commands
import logging

logging.basicConfig(level=logging.INFO)

async def on_startup(dp):
        from handler import message
        await set_default_commands(dp)

if __name__ == '__main__':
        from aiogram import executor
        from config.config import dp
        executor.start_polling(dp, skip_updates=True, allowed_updates=[
                'message', 
                'chat_member', 
                'my_chat_member', 
                'callback_query'
                ],  on_startup=on_startup)