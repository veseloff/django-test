# from tg_bot.bot.bot.loader import dp
# # from tg_bot.bot.config import admin_id
#
#
# async def on_shutdown(dp):
#     await dp.close()
#
#
# if __name__ == '__main__':
#     from aiogram import executor
#     from tg_bot.bot.bot.handlers import dp
#
#     executor.start_polling(dp, on_shutdown=on_shutdown)

from aiogram import executor

# from config import admin_id
from loader import bot


async def on_shutdown(dp):
    await bot.close()

#
# async def on_startup(dp):
#     await bot.send_message(admin_id, "Я запущен!")


if __name__ == '__main__':
    from handler import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
