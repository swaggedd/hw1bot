from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Привет, Я загадал число от 1 до 3, угадай его')
@dp.message_handler()
async def guess(message:types.Message):
    user = int(message.text)
    rand = random.randint(1,3)
    if user == rand:
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

executor.start_polling(dp)
