from loader import bot
import asyncio
import requests
from config import TOKEN
# async def write_code_new_user(link, code):
#     await bot.send_message(chat_id=link, text=f'Код для авторизации {code}')
#
#
# async def main():
#     task = asyncio.create_task(write_code_new_user('tea_coffeee_dance', 1234))
#     await task
#
# asyncio.run(main())

requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=413900526&text={123}&parse_mode=HTML")