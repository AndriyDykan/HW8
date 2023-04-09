from datetime import datetime, timedelta
from collections import defaultdict
from pprint import pprint


def get_start_date(data: datetime):
    week = 7 - data.weekday()
    return data + timedelta(days=week)


def normilized_date(text, start, end):
    data = datetime.strptime(text, "%d,%m,%Y")
    if start <= data.replace(year=start.year) <= end:
        return data.replace(year=start.year)
    if start <= data.replace(year=end.year) <= end:
        return data.replace(year=end.year)


def get_birthdays_per_week(user):
    birthsdays = defaultdict(list)
    today = datetime.now()
    #today = datetime(year=2023, month=12, day=25)
    start = get_start_date(today) - timedelta(2)
    end = start + timedelta(6)
    print(start)
    print(end)
    for i in user:
        flag = normilized_date(i["birthday"], start, end)
        if flag:
            if flag.weekday() in (5, 6):
                birthsdays["Monday"].append(i["name"])
            else:
                birthsdays[flag.strftime("%A")].append(i["name"])
    return pprint(birthsdays)


if __name__ == "__main__":
    user = [{"name": "Andriy", "birthday": "10,04,2004"},
            {"name": "denis", "birthday": "1,04,2004"},
            {"name": "Katya", "birthday": "16,04,2004"},
            {"name": "illja", "birthday": "24,12,2004"},
            {"name": "sergiy", "birthday": "25,12,2004"},
            {"name": "volodiay", "birthday": "1,1,2005"},
            {"name": "danilo", "birthday": "2,1,2005"},
            {"name": "kruk", "birthday": "3,1,2005"},
            {"name": "ela", "birthday": "4,1,2005"},
            {"name": "natalia", "birthday": "5,1,2005"},
            {"name": "Yura", "birthday": "6,1,2005"},
            {"name": "dantist", "birthday": "7,1,2005"}
            ]
    get_birthdays_per_week(user)
