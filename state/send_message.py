from aiogram.dispatcher.filters.state import State, StatesGroup

class for_send(StatesGroup):
    permission_send = State()
    permission_send_forward = State()
    permission_group = State()
    permission_send_forward_user = State()
