import requests


class NalogRuPython:
    HOST = 'irkkt-mobile.nalog.ru:8888'
    DEVICE_OS = 'iOS'
    CLIENT_VERSION = '2.9.0'
    DEVICE_ID = '7C82010F-16CC-446B-8F66-FC4080C66521'
    ACCEPT = '*/*'
    USER_AGENT = 'billchecker/2.9.0 (iPhone; iOS 13.6; Scale/2.00)'
    ACCEPT_LANGUAGE = 'ru-RU;q=1, en-US;q=0.9'
    CLIENT_SECRET = 'IyvrAbKt9h/8p6a7QPh8gpkXYQ4='
    OS = 'Android'
    HEADERS = {
            'Host': HOST,
            'Accept': ACCEPT,
            'Device-OS': DEVICE_OS,
            'Device-Id': DEVICE_ID,
            'clientVersion': CLIENT_VERSION,
            'Accept-Language': ACCEPT_LANGUAGE,
            'User-Agent': USER_AGENT,
        }

    def __init__(self, phone):
        self.__session_id = None
        self.set_session_id(phone)

    def set_session_id(self, phone) -> None:
        """
        Authorization using phone and SMS code
        """
        self.__phone = phone

        url = f'https://{self.HOST}/v2/auth/phone/request'
        payload = {
            'phone': self.__phone,
            'client_secret': self.CLIENT_SECRET,
            'os': self.OS
        }
        resp = requests.post(url, json=payload, headers=self.HEADERS)

    def code_confirmation(self, code):
        self.__code = code

        url = f'https://{self.HOST}/v2/auth/phone/verify'
        payload = {
            'phone': self.__phone,
            'client_secret': self.CLIENT_SECRET,
            'code': self.__code,
            "os": self.OS
        }

        resp = requests.post(url, json=payload, headers=self.HEADERS)
        if resp.status_code == 200:
            self.__session_id = resp.json()['sessionId']
            self.__refresh_token = resp.json()['refresh_token']
            return 200
        else:
            return 402

    def _get_ticket_id(self, qr: str):
        url = f'https://{self.HOST}/v2/ticket'
        payload = {'qr': qr}
        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'sessionId': self.__session_id,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)

        return resp.json()["id"]

    def get_ticket(self, qr: str):
        ticket_id = self._get_ticket_id(qr)
        url = f'https://{self.HOST}/v2/tickets/{ticket_id}'
        headers = {
            'Host': self.HOST,
            'sessionId': self.__session_id,
            'Device-OS': self.DEVICE_OS,
            'clientVersion': self.CLIENT_VERSION,
            'Device-Id': self.DEVICE_ID,
            'Accept': self.ACCEPT,
            'User-Agent': self.USER_AGENT,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'Content-Type': 'application/json'
        }

        resp = requests.get(url, headers=headers)

        return resp.json()
