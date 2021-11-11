import requests
import re
from tg_bot.bot.bot.loader import dp, bot, db
from aiogram.types import Message
from tg_bot.bot.bot.nalog_python import NalogRuPython
from tg_bot.bot.bot.fnl_requests import json_parser



@dp.message_handler(content_types=['document', 'photo'])
async def handle_docs_photo(message: Message):
    if message.document is None:
        await message.photo[-1].download('чек1.jpg')
        filename = 'чек1.jpg'
    else:
        await message.document.download('чек2.jpg')
        filename = 'чек2.jpg'
    client = NalogRuPython()
    qr_code = get_info_zxing_qrscanner(filename)
    ticket = client.get_ticket(qr_code)
    data_checka = json_parser(ticket)
    result_answer = ""
    for el in data_checka[1]:
        result_answer = result_answer + '\n' + el
    await message.answer(f"{data_checka[0]} Вы купили: {result_answer}  \n \n Потратив всего: {data_checka[2]} \u20bd")


@dp.message_handler()
async def exo(message: Message):
    await message.answer(f'Ты написал {message.text}.\n Я жду команду /start')
    await message.photo[0].download()


def qrcode_scanner(url, filename):
    """
        отправляет запрос в онлайн сканер qr кодов и получает ответ от сервера (Отправка файла через Request Payload)
        url - ссылка на скрипт онлайн сканера
        filename  - путь до файла снимка где находится фотография с qr кодом
    """
    with open(filename, 'rb') as f:
        r = requests.post(url, files={filename: f})
        result = {"code": r.status_code, "text": r.text}
    return result


def get_info_zxing_qrscanner(filename):
    url = "https://zxing.org/w/decode"
    rr = qrcode_scanner(url, filename)
    s = rr["text"]
    pattern = r't=[0-9T]+&amp;s=[0-9.]+&amp;fn=[0-9]+&amp;i=[0-9.]+&amp;fp=[0-9]+&amp;n=[0-9]+'
    result = re.findall(pattern, s)[0].replace("amp;", '')

    return str(result)



