from aiogram import executor
from loader import bot


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    from handler import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
