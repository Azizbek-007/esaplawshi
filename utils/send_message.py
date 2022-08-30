import asyncio
from aiogram.utils import exceptions

async def send_message(user_id: int, msg) -> bool:

    try:
        await msg.copy_to(chat_id=user_id, reply_markup=msg.reply_markup)
    except exceptions.BotBlocked:
        pass
    except exceptions.ChatNotFound:
        pass
    except exceptions.RetryAfter as e:
        await asyncio.sleep(e.timeout)
        await msg.copy_to(chat_id=user_id, reply_markup=msg.reply_markup)
    except exceptions.UserDeactivated:
        pass
    except exceptions.MigrateToChat as e:
        try:
            await msg.copy_to(chat_id=e.migrate_to_chat_id, reply_markup=msg.reply_markup)
        except:
            pass
    except exceptions.TelegramAPIError:
        pass
    else:
        pass
        return True
    return False