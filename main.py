from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '#############################'
TEXT = 'hi'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def echo(message: types.Message):
    await bot.approve_chat_join_request(
            message.chat.id,
            message.from_user.id
        )
    await bot.send_message(
            message.from_user.id,
            TEXT
        )

if __name__ == '__main__':
    executor.start_polling(dp)
