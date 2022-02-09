import aiogram
from aiogram import Bot, types, Dispatcher
from aiogram import executor
from aiogram.utils.mixins import T
from m import tet


tt = '2123644700:AAGJAyLTtCJUC-H6wSdqeWkQYNp8s_rhQf4'
bot = Bot(token=tt)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Пупок залупок')

@dp.message_handler(text='пупок лох')
async def py(message: types.Message):
    await message.answer(tet)

if __name__ == "__main__":
    executor.start_polling(dp)