import asyncio
import logging
import sys
import json

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, URLInputFile , ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from commands import (MOUSES_COMMAND, KEYBOARDS_COMMAND, HEADPHONES_COMMAND, MICROPHONE_COMMAND,
                      MOUSES_COMMAND_BOT, KEYBOARDS_COMMAND_BOT, MICROPHONE_COMMAND_BOT,
                      HEADPHONES_COMMAND_BOT, START_COMMAND_BOT, DEVICE_BY_COST_COMMAND_BOT, DEVICE_BY_COST_COMMAND)

from config import BOT_TOKEN as TOKEN

from state import DeviceForm

from keyboards import (mouses_keyboards_markup, MousesCallback,
                       keyboards_keyboards_markup, KeyboardsCallback,
                       headphones_keyboards_markup, HeadphonesCallback,
                       microphones_keyboards_markup, MicrophonesCallback)

from model import Mouse, Keyboard, Headphone, Microphone ,Device

dp = Dispatcher()


button_mouse = KeyboardButton(text='mouse')
button_keyboard = KeyboardButton(text='keyboard')
button_headphones = KeyboardButton(text='headphones')
button_microphone = KeyboardButton(text='microphone')

buttons = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [button_mouse, button_keyboard],
    [button_headphones, button_microphone]
])
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! \n"
                         f"I'am Device bot and i'll help you to choose devices\n"
                         f"Headphones , mouse , keyboard or microphone. Choose by cost =)\n"
                         f"\n"
                         f"All comands:\n\n"
                         f"/start\n"
                         f"/mouses\n"
                         f"/keyboards\n"
                         f"/headphones\n"
                         f"/microphones\n"
                         f"/device_by_cost")


@dp.message(DEVICE_BY_COST_COMMAND)
async def command_device_by_cost_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(DeviceForm.type)
    await message.answer(f'Choose in buttons a type device\n', reply_markup=buttons)


@dp.message(DeviceForm.type)
async def device_type(message: Message, state: FSMContext) -> None:
    await state.update_data(type=message.text.lower())
    await state.set_state(DeviceForm.cost)
    await message.answer(f'Write cost\n'
                         f'"500","1000"...', reply_markup=ReplyKeyboardRemove())


@dp.message(DeviceForm.cost)
async def device_cost(message: Message, state: FSMContext) -> None:
    data = await state.update_data(cost=int(message.text))
    device = Device(**data)
    await state.clear()

    costed_devices = []

    match device.type:
        case 'mouse':
            mouse_data = get_mouses()
            for mouse in mouse_data:
                if mouse.get('cost') <= device.cost:
                    costed_devices.append(mouse)
            for mouse in costed_devices:
                mouse = Mouse(**mouse)
                text = f"Name: {mouse.name}\n" \
                       f"Company: {mouse.company}\n" \
                       f"Cost: {mouse.cost} UAH\n" \
                       f"Rate: {mouse.rating}\n" \
                       f"Description: {mouse.description}\n" \

                await message.answer_photo(caption=text, photo=URLInputFile(mouse.photo,
                                                                                        filename=f'{mouse.name}_photo.{mouse.photo.split('.')[-1]}'))
        case 'keyboard':
            headphones_data = get_keyboards()
            for keyboard in headphones_data:
                if keyboard.get('cost') <= device.cost:
                    costed_devices.append(keyboard)
            for keyboard in costed_devices:
                keyboard = Mouse(**keyboard)
                text = f"Name: {keyboard.name}\n" \
                       f"Company: {keyboard.company}\n" \
                       f"Cost: {keyboard.cost} UAH\n" \
                       f"Rate: {keyboard.rating}\n" \
                       f"Description: {keyboard.description}\n" \

                await message.answer_photo(caption=text, photo=URLInputFile(keyboard.photo,
                                                                            filename=f'{keyboard.name}_photo.{keyboard.photo.split('.')[-1]}'))
        case 'headphones':
            headphones_data = get_headphones()
            for headphones in headphones_data:
                if headphones.get('cost') <= device.cost:
                    costed_devices.append(headphones)
            for headphones in costed_devices:
                headphones = Mouse(**headphones)
                text = f"Name: {headphones.name}\n" \
                       f"Company: {headphones.company}\n" \
                       f"Cost: {headphones.cost} UAH\n" \
                       f"Rate: {headphones.rating}\n" \
                       f"Description: {headphones.description}\n" \

                await message.answer_photo(caption=text, photo=URLInputFile(headphones.photo,
                                                                            filename=f'{headphones.name}_photo.{headphones.photo.split('.')[-1]}'))
        case 'microphone':
            microphone_data = get_microphones()
            for microphone in microphone_data:
                if microphone.get('cost') <= device.cost:
                    costed_devices.append(microphone)
            for microphone in costed_devices:
                microphone = Mouse(**microphone)
                text = f"Name: {microphone.name}\n" \
                       f"Company: {microphone.company}\n" \
                       f"Cost: {microphone.cost} UAH\n" \
                       f"Rate: {microphone.rating}\n" \
                       f"Description: {microphone.description}\n" \

                await message.answer_photo(caption=text, photo=URLInputFile(microphone.photo,
                                                                            filename=f'{microphone.name}_photo.{microphone.photo.split('.')[-1]}'))









@dp.message(MOUSES_COMMAND)
async def command_mouses_handler(message: Message) -> None:
    data = get_mouses()
    markup = mouses_keyboards_markup(mouses_list=data)
    await message.answer(
        f'List mouses . Click for details ...', reply_markup=markup
    )



@dp.callback_query(MousesCallback.filter())
async def callb_mouse(callback: CallbackQuery, callback_data: MousesCallback) -> None:
    mouse_id = callback_data.id
    mouse_data = get_mouses(mouse_id=mouse_id)
    mouse = Mouse(**mouse_data)

    text = f"Name: {mouse.name}\n" \
           f"Company: {mouse.company}\n" \
           f"Cost: {mouse.cost} UAH\n" \
           f"Rate: {mouse.rating}\n" \
           f"Description: {mouse.description}\n" \

    await callback.message.answer_photo(caption=text, photo=URLInputFile(mouse.photo,
                                                                         filename=f'{mouse.name}_photo.{mouse.photo.split('.')[-1]}'))


@dp.message(KEYBOARDS_COMMAND)
async def command_keyboards_handler(message: Message) -> None:
    data = get_keyboards()
    markup = keyboards_keyboards_markup(keyboards_list=data)
    await message.answer(
        f'List keyboards . Click for details ...', reply_markup=markup
    )


@dp.callback_query(KeyboardsCallback.filter())
async def callb_keyboard(callback: CallbackQuery, callback_data: KeyboardsCallback) -> None:
    keyboard_id = callback_data.id
    keyboard_data = get_keyboards(keyboard_id=keyboard_id)
    keyboard = Keyboard(**keyboard_data)

    text = f"Name: {keyboard.name}\n" \
           f"Company: {keyboard.company}\n" \
           f"Cost: {keyboard.cost} UAH\n" \
           f"Rate: {keyboard.rating}\n" \
           f"Description: {keyboard.description}\n" \

    await callback.message.answer_photo(caption=text, photo=URLInputFile(keyboard.photo,
                                                                         filename=f'{keyboard.name}_photo.{keyboard.photo.split('.')[-1]}'))


@dp.message(HEADPHONES_COMMAND)
async def command_headphones_handler(message: Message) -> None:
    data = get_headphones()
    markup = headphones_keyboards_markup(headphones_list=data)
    await message.answer(
        f'List headphones . Click for details ...', reply_markup=markup
    )


@dp.callback_query(HeadphonesCallback.filter())
async def callb_headphone(callback: CallbackQuery, callback_data: HeadphonesCallback) -> None:
    headphone_id = callback_data.id
    headphone_data = get_headphones(headphone_id=headphone_id)
    headphone = Headphone(**headphone_data)

    text = f"Name: {headphone.name}\n" \
           f"Company: {headphone.company}\n" \
           f"Cost: {headphone.cost} UAH\n" \
           f"Rate: {headphone.rating}\n" \
           f"Description: {headphone.description}\n" \

    await callback.message.answer_photo(caption=text, photo=URLInputFile(headphone.photo,
                                                                         filename=f'{headphone.name}_photo.{headphone.photo.split('.')[-1]}'))


@dp.message(MICROPHONE_COMMAND)
async def command_microphones_handler(message: Message) -> None:
    data = get_microphones()
    markup = microphones_keyboards_markup(microphones_list=data)
    await message.answer(
        f'List microphones . Click for details ...', reply_markup=markup
    )


@dp.callback_query(MicrophonesCallback.filter())
async def callb_microphone(callback: CallbackQuery, callback_data: MicrophonesCallback) -> None:
    microphone_id = callback_data.id
    microphone_data = get_microphones(microphone_id=microphone_id)
    microphone = Microphone(**microphone_data)

    text = f"Name: {microphone.name}\n" \
           f"Company: {microphone.company}\n" \
           f"Cost: {microphone.cost} UAH\n" \
           f"Rate: {microphone.rating}\n" \
           f"Description: {microphone.description}\n" \

    await callback.message.answer_photo(caption=text, photo=URLInputFile(microphone.photo,
                                                                         filename=f'{microphone.name}_photo.{microphone.photo.split('.')[-1]}'))


def get_mouses(file_path: str = "mouses_data.json", mouse_id: int | None = None ) -> list[dict] | dict:
    with open(file_path, 'r', encoding='utf-8') as fp:
        mouses = json.load(fp)
        if mouse_id != None and mouse_id < len(mouses):
            return mouses[mouse_id]
    return mouses


def get_keyboards(file_path: str = "keyboards_data.json", keyboard_id: int | None = None) -> list[dict] | dict:
    with open(file_path, 'r', encoding='utf-8') as fp:
        keyboards = json.load(fp)
        if keyboard_id != None and keyboard_id < len(keyboards):
            return keyboards[keyboard_id]
    return keyboards


def get_headphones(file_path: str = "headphones_data.json", headphone_id: int | None = None) -> list[dict] | dict:
    with open(file_path, 'r', encoding='utf-8') as fp:
        headphones = json.load(fp)
        if headphone_id != None and headphone_id < len(headphones):
            return headphones[headphone_id]
    return headphones


def get_microphones(file_path: str = "microphones_data.json", microphone_id: int | None = None) -> list[dict] | dict:
    with open(file_path, 'r', encoding='utf-8') as fp:
        microphones = json.load(fp)
        if microphone_id != None and microphone_id < len(microphones):
            return microphones[microphone_id]
    return microphones


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands([
        START_COMMAND_BOT, MOUSES_COMMAND_BOT, KEYBOARDS_COMMAND_BOT, HEADPHONES_COMMAND_BOT, MICROPHONE_COMMAND_BOT,DEVICE_BY_COST_COMMAND_BOT
    ])

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
