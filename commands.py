from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand

MOUSES_COMMAND = Command('mouses')
KEYBOARDS_COMMAND = Command('keyboards')
HEADPHONES_COMMAND = Command('headphones')
MICROPHONE_COMMAND = Command('microphones')
DEVICE_BY_COST_COMMAND = Command('device_by_cost')


MOUSES_COMMAND_BOT = BotCommand(command='mouses',description='Choose mouse')
KEYBOARDS_COMMAND_BOT = BotCommand(command='keyboards',description='Choose keyboard')
HEADPHONES_COMMAND_BOT = BotCommand(command='headphones',description='Choose headphones')
MICROPHONE_COMMAND_BOT = BotCommand(command='microphones',description='Choose microphone')
DEVICE_BY_COST_COMMAND_BOT = BotCommand(command='device_by_cost',description='Find device by cost')

START_COMMAND_BOT = BotCommand(command='start',description='Start bot')