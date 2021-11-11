from loader import bot


async def write_code_new_user(link):
    await bot.send_message(chat_id=link, text='Привет, я бот помощник, помогу тебе составить отчёт по чекам')
