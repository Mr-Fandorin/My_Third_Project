def filter_by_currency(transactions, currency):
    filtered_people = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    i = 0
    while True:
        yield filtered_people[i]
        i += 1


def transaction_descriptions(transactions):
    i = 0
    while True:
        yield transactions[i]["description"]
        i += 1


def card_number_generator(a, b):
    x = a
    while x <= b:
        str_card_num = "0000000000000000"
        lenght_num = len(str(x))
        new_num = str_card_num[:16 - lenght_num]
        full_num = new_num + str(x)
        yield f"{full_num[:4]} {full_num[4:8]} {full_num[8:12]} {full_num[12:]}"
        x += 1
