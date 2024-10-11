from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MousesCallback(CallbackData, prefix='mouse', sep=";"):
    id: int
    name: str


def mouses_keyboards_markup(mouses_list: list[dict]):
    builder = InlineKeyboardBuilder()

    for index, mouse_data in enumerate(mouses_list):
        callback_data = MousesCallback(id=index, **mouse_data)
        builder.button(
            text=f'{callback_data.name}',
            callback_data=callback_data.pack()
        )

    builder.adjust(1, repeat=True)
    return builder.as_markup()


class KeyboardsCallback(CallbackData, prefix='keyboard', sep=";"):
    id: int
    name: str


def keyboards_keyboards_markup(keyboards_list: list[dict]):
    builder = InlineKeyboardBuilder()

    for index, keyboard_data in enumerate(keyboards_list):
        callback_data = KeyboardsCallback(id=index, **keyboard_data)
        builder.button(
            text=f'{callback_data.name}',
            callback_data=callback_data.pack()
        )

    builder.adjust(1, repeat=True)
    return builder.as_markup()


class HeadphonesCallback(CallbackData, prefix='headphone', sep=";"):
    id: int
    name: str


def headphones_keyboards_markup(headphones_list: list[dict]):
    builder = InlineKeyboardBuilder()

    for index, headphone_data in enumerate(headphones_list):
        callback_data = HeadphonesCallback(id=index, **headphone_data)
        builder.button(
            text=f'{callback_data.name}',
            callback_data=callback_data.pack()
        )

    builder.adjust(1, repeat=True)
    return builder.as_markup()


class MicrophonesCallback(CallbackData, prefix='microphone', sep=";"):
    id: int
    name: str


def microphones_keyboards_markup(microphones_list: list[dict]):
    builder = InlineKeyboardBuilder()

    for index, microphone_data in enumerate(microphones_list):
        callback_data = MicrophonesCallback(id=index, **microphone_data)
        builder.button(
            text=f'{callback_data.name}',
            callback_data=callback_data.pack()
        )

    builder.adjust(1, repeat=True)
    return builder.as_markup()

