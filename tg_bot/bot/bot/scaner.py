import requests
import re


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