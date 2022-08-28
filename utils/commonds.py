from aiogram.types import BotCommand

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        BotCommand("start", "Запустить бота"),
        BotCommand("help", "Barcha buyruqlar haqida"),
        BotCommand("mymembers", "siz qoshgan odamlar soni!"),
        BotCommand("yourmembers", "Reply qilingan odam qoshgan odamlar soni!"),
        BotCommand("top", "Eng kop odam qoshgan 10 talik"),
    ])