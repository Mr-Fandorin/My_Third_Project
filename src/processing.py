from collections import Counter
from typing import Union
import re

def filter_by_state(list_of_user_dates: list[dict], state: str = "EXECUTED") -> Union[str, list[dict]]:
    """Функция, фильтрующая словари по нужному ключу"""
    new_list_of_users = []
    for item in list_of_user_dates:
        for value in item.values():
            if value == state:
                new_list_of_users.append(item)
    if new_list_of_users == []:
        return "нет данных"
    else:
        return new_list_of_users


def sort_by_date(list_of_user_dates: list[dict], sorting_type: bool = True) -> list[dict]:
    """Функция, сортирующая словари по нужному ключу"""
    sorted_list_of_users = sorted(list_of_user_dates, key=lambda dict_user: dict_user["date"], reverse=sorting_type)
    return sorted_list_of_users


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    new_list = []
    for item in data:
        if re.findall(search, item['description'].lower(), flags=0):
            new_list.append(item)
    return new_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    new_list = []
    for item in data:
        for category in categories:
            if category == item['description']:
                new_list.append(item['description'])
            else:
                continue
    counted = Counter(new_list)
    dict_counted = dict(counted)
    return dict_counted





# dict_test = [
#     {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
#      'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#      'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
#      'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
#      'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
#     {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
#      'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#      'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},
#     {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
#      'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
#     {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
#      'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#      'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'},
#     {'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246',
#      'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод организации', 'from': 'Счет 10848359769870775355', 'to': 'Счет 21969751544412966366'},
#     {'id': 522357576, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230',
#      'operationAmount': {'amount': '51463.70', 'currency': {'name': 'USD', 'code': 'USD'}},
#      'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'}]
#
# print(process_bank_search(dict_test, 'открытие'))