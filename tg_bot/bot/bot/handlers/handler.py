import logging
import requests
from tg_bot.bot.bot.loader import dp
from aiogram.types import Message


@dp.message_handler(content_types=['document', 'photo'])
async def handle_docs_photo(message: Message):
    logging.info('зашёл в метод')
    if message.document is None:
        await message.photo[-1].download('чек1.jpg')
        filename = 'чек1.jpg'
    else:
        await message.document.download('чек2.jpg')
        filename = 'чек2.jpg'
    data = parse_data(get_info_zxing_qrscanner(filename))
    await message.answer(f'{data[0]} вы совершили покупку на {data[1]} рублей')
    logging.info('fff')


@dp.message_handler()
async def exo(message: Message):
    await message.answer(f'Ты написал {message.text}.\n Я жду команду /start')
    await message.photo[0].download()


def parse_data(data):
    date = data[2:9]
    sum = data[22:25]
    fn = data[37:52]
    fp = data[71:80]
    return date, sum, fn, fp


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
    i = s.find("pre")
    s = s[i + 4:]
    i = s.find("pre")
    s = s[:i]
    s = s.strip("/")
    s = s.strip("<")
    s = s.strip(">")
    return s
