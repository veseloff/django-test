from tg_bot.bot.bot.loader import bot
# from tg_bot.bot.config import admin_id


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor
    from tg_bot.bot.bot.handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)
