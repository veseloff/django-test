import time
import datetime


def json_parser(json):
    months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря"
    }

    date_time_str = json["operation"]["date"]
    check_amount = json["operation"]["sum"] / 100
    items = []
    for item in json["ticket"]["document"]["receipt"]["items"]:
        items.append(f"* {item['name']} - {str(item['sum']/100)} \u20bd")
    date = time.strptime(date_time_str, "%Y-%m-%dT%H:%M")
    time_res = f"{date.tm_mday} {months[date.tm_mon]} {date.tm_year} года"
    date = datetime.datetime(date.tm_year, date.tm_mon, date.tm_mday, date.tm_hour, date.tm_min)
    return time_res, items, check_amount, date

