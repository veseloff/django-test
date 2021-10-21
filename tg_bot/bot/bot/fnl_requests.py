import datetime


def json_parser(json):
    date = json["operation"]["date"]
    total_sum = json["operation"]["sum"]/100
    items = []
    for item in json["ticket"]["document"]["receipt"]["items"]:
        items.append(str(item["name"]) + " " + str(item["sum"]/100))
    shop = json["ticket"]["document"]["receipt"]["retailPlace"]
    #datetime.datetime.strpftime("%YYYY-%MM-%DD")
    return f"{date} вы купили: {items}, потратив всего: {total_sum}"
