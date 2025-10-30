def filter_by_currency(transactions, currency):
    filtered_people = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    i = 0
    while True:
        yield filtered_people[i]
        i += 1


