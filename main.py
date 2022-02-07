from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import read_excel
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["Время_пар"])
async def time_lesson(message: types.Message):
    await bot.send_message(message.from_user.id, '\n'.join(map(str, read_excel.parse_time())))

@dp.message_handler(commands=["Список_групп"])
async def groups(message: types.Message):
    await bot.send_message(message.from_user.id, '\n'.join(map(str, read_excel.parse_groups())))

"""@dp.message_handler(commands=["Выберете_номер_группы"])
async def write_group(message: types.Message):
    group_num = message.text

    await bot.send_message(message.from_user.id, )

@dp.message_handler(commands=["День_недели"])
async def write_day(messge:types.Message):
    day = messge.text"""
@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dp, skip_updates=True)