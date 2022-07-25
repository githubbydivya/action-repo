from datetime import timezone, datetime

import pytz as pytz
from dateutil.parser import parse


# from python-dateutil import dateutil

def special_nth_day(formatted_date: str,
                    dic={'1': 'st', '2': 'nd', '3': 'rd'}):
    formatted_date_list = list(formatted_date)
    char_date_0 = formatted_date_list[0]
    char_date_1 = formatted_date_list[1]
    if char_date_0 == '1':
        formatted_date_list[2] = 'th'
    elif char_date_0 == '0' or char_date_0 == '2' or char_date_0 == '3':
        val_from_dic = None
        if char_date_1 in dic:
            val_from_dic = dic[char_date_1]
        if val_from_dic:
            formatted_date_list[2] = val_from_dic
        else:
            formatted_date_list[2] = 'th'

    formatted_date_list_new = ''.join(formatted_date_list)
    return formatted_date_list_new


def check_method():
    print("Hello World")


check_method()
print("Welcome To Webhook Action Repo")

print("Testing Webhook-impl-two repo")


def parse_date_convert(date, fmt=None):
    if fmt is None:
        fmt = '%Y-%m-%d %H:%M:%S %Z'  # Defaults to : 2022-08-31 07:47:30
    get_date_obj = parse(str(date))
    return str(get_date_obj.strftime(fmt))


date_val = '2022-07-25T14:35:48+05:30'
datestring = '2022-07-27T14:52:28+05:30'
datezString = '2022-07-24T09:22:28Z'
# d = dateutil.parser.parse(datestring)
# dtutc = date_val.astimezone(timezone.utc)
print(parse_date_convert(date_val))
print(parse_date_convert(datestring))
print(parse_date_convert(datezString))

so = datetime.fromisoformat(date_val).astimezone(pytz.utc)
so_1 = datetime.fromisoformat(datestring).astimezone(pytz.utc)
# so_2 = datetime.fromisoformat(datezString).astimezone(pytz.utc)
# datetime.datetime.strptime(date_val, '%Y-%m-%dT%H:%M:%S%z').astimezone(pytz.utc)
print("so:", so, so_1)

months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
date = '2021-11-21 11:22:03'
# month = date.dt.month
# month_name = months_in_year[month - 1]
dt_obj = datetime.strptime(datestring, '%Y-%m-%dT%H:%M:%S%z')
dt_obj_utc = dt_obj.astimezone(timezone.utc)
print(dt_obj_utc.strftime("%d %c %B %Y %H:%M %p %Z"))
print(special_nth_day(dt_obj_utc.strftime("%d  %B %Y %H:%M %p %Z")))
