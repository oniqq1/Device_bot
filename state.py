from aiogram.fsm.state import State, StatesGroup


class MouseForm(StatesGroup):
    name = State()
    company = State()
    cost = State()
    rating = State()
    description = State()
    photo = State()


class KeyboardsForm(StatesGroup):
    name = State()
    company = State()
    cost = State()
    rating = State()
    description = State()
    photo = State()


class HeadphonesForm(StatesGroup):
    name = State()
    company = State()
    cost = State()
    rating = State()
    description = State()
    photo = State()


class MicrophoneForm(StatesGroup):
    name = State()
    company = State()
    cost = State()
    rating = State()
    description = State()
    photo = State()

class DeviceForm(StatesGroup):
    type = State()
    cost = State()