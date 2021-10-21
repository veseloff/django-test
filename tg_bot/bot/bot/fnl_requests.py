import datetime
import time as t
# time_s = t.strptime('2021-11-02', "%Y-%m-%d")
#
# print(t.strftime('%d-%m-%Y', time_s)) -> #tuple is converted to string-format
# print(time_s.tm_mday, time_s.tm_mon, time_s.tm_year)

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
    date = json["operation"]["date"]
    total_sum = json["operation"]["sum"]/100
    items = []
    for item in json["ticket"]["document"]["receipt"]["items"]:
        items.append(f"* {item['name']} - {str(item['sum']/100)} \u20bd")  # + " " + str(item["sum"]/100) f"- {item["name"]} {str(item["sum"]/100)}}"
    shop = json["ticket"]["document"]["receipt"]["retailPlace"]
    time_s = t.strptime(date[:10], "%Y-%m-%d")
    time_res = f"{time_s.tm_mday} {months[time_s.tm_mon]} {time_s.tm_year} года"
    return time_res, items, total_sum

# f"{time_res} Вы купили: {items}, потратив всего: {total_sum}"