from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    "Генератор функции сортировки базы данных по заданной валюте"
    filtered_people = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    if not filtered_people:
        yield "Нет данных"
    else:
        i = 0
        while True:
            if len(filtered_people) >= i:
                yield filtered_people[i]
                i += 1
            else:
                break


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    "Генератор функции вывода описаний транзакций"
    if not transactions:
        yield "Нет данных"
    else:
        i = 0
        while True:
            if len(transactions) >= i:
                yield transactions[i]["description"]
                i += 1
            else:
                break


def card_number_generator(a: int, b: int) -> Iterator:
    "Генератор функции генерирования номеров карт в заданном диапазоне"
    x = a
    while x <= b:
        str_card_num = "0000000000000000"
        lenght_num = len(str(x))
        if lenght_num <= 16:
            str_card_num = f"{x:016d}"
            yield f"{str_card_num[:4]} {str_card_num[4:8]} {str_card_num[8:12]} {str_card_num[12:]}"
            x += 1
        else:
            yield "неверный номер карты"
