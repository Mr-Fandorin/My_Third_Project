from typing import Union


def filter_by_currency(transactions: list[dict], currency: str) -> Union[str, list[dict]]:
    filtered_people = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    if not filtered_people:
        yield "Нет данных"
    else:
        i = 0
        while True:
            yield filtered_people[i]
            i += 1


def transaction_descriptions(transactions: list[dict]) -> Union[str, list[dict]]:
    if not transactions:
        yield "Нет данных"
    else:
        i = 0
        while True:
            yield transactions[i]["description"]
            i += 1


def card_number_generator(a: int, b: int) -> str:
    x = a
    while x <= b:
        str_card_num = "0000000000000000"
        lenght_num = len(str(x))
        if lenght_num > 16:
            yield "неверный номер карты"
        else:
            new_num = str_card_num[: 16 - lenght_num]
            full_num = new_num + str(x)
            yield f"{full_num[:4]} {full_num[4:8]} {full_num[8:12]} {full_num[12:]}"
            x += 1
