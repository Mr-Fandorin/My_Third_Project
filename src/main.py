from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.transactions import reader_csv_transactions, reader_excel_transaction
from src.utils import operations_data
from src.widget import get_date, mask_account_card


def main():
    """Функция, предоставляющая пользователю информацию о банковских операциях по его запросу"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    num_menu = int(input())
    if num_menu == 1:
        """Если пользователь выбрал обработку файла JSON"""
        print("Для обработки выбран JSON-файл.\n")
        list_transactions = operations_data("../data/operations.json")
        for item in list_transactions:
            """Приводим данные из файла JSON в общий формат"""
            try:
                item["amount"] = item["operationAmount"]["amount"]
                item["currency_name"] = item["operationAmount"]["currency"]["name"]
                item["currency_code"] = item["operationAmount"]["currency"]["code"]
                del item["operationAmount"]
            except KeyError:
                continue

    elif num_menu == 2:
        """Если пользователь выбрал обработку файла CSV"""
        print("Для обработки выбран CSV-файл.\n")
        list_transactions = reader_csv_transactions("../data/transactions.csv")
    elif num_menu == 3:
        """Если пользователь выбрал обработку файла Excel"""
        print("Для обработки выбран XLSX-файл.\n")
        list_transactions = reader_excel_transaction("../data/transactions_excel.xlsx")

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        name_operation = input().upper()
        if name_operation == "EXECUTED":
            """Если пользователь выбрал сортировку по 'EXECUTED'"""
            print('Операции отфильтрованы по статусу "EXECUTED"\n')
            filter_list = filter_by_state(list_transactions)
            if filter_list == "нет данных":
                return "Нет данных"
            else:
                break
        elif name_operation == "CANCELED":
            """Если пользователь выбрал сортировку по 'CANCELED'"""
            print('Операции отфильтрованы по статусу "CANCELED"\n')
            filter_list = filter_by_state(list_transactions, "CANCELED")
            if filter_list == "нет данных":
                return "Нет данных"
            else:
                break
        elif name_operation == "PENDING":
            """Если пользователь выбрал сортировку по 'PENDING'"""
            print('Операции отфильтрованы по статусу "PENDING"\n')
            filter_list = filter_by_state(list_transactions, "PENDING")
            if filter_list == "нет данных":
                return "Нет данных"
            else:
                break
        else:
            print(f"Статус операции {name_operation} недоступен.\n")
            continue

    print("Отсортировать операции по дате? Да/Нет")
    sort_date = input().lower()
    if sort_date == "да":
        """Если пользователь выбрал сортировку по дате"""
        print("Отсортировать по возрастанию или по убыванию?")
        sort_up_down = input().lower()
        if sort_up_down == "по возрастанию":
            """Если пользователь выбрал сортировку по возрастанию"""
            filter_list = sort_by_date(filter_list, False)
        elif sort_up_down == "по убыванию":
            """Если пользователь выбрал сортировку по убыванию"""
            filter_list = sort_by_date(filter_list)

    print("Выводить только рублевые транзакции? Да/Нет")
    sort_currency = input().lower()
    if sort_currency == "да":
        """Если пользователь выбрал вывод операций только в рублях"""
        result_list = []
        test_list = filter_by_currency(filter_list, "RUB")
        for item in test_list:
            result_list.append(item)
        filter_list = result_list

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_answer = input().lower()
    if user_answer == "да":
        """Если пользователь выбрал сортировку по ключевому слову в описании"""
        print("Введите слово в описании")
        sort_by_word = input().lower()
        filter_list = process_bank_search(filter_list, sort_by_word)

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filter_list)}")
    if filter_list == []:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        for item in filter_list:
            """Выводим результат"""
            date_of_transction = get_date(item["date"])
            category_of_transaction = item["description"]
            transfer_to = mask_account_card(item["to"])

            amount = item["amount"]
            currency_code = item["currency_code"]
            print(f"{date_of_transction} {category_of_transaction}")
            if category_of_transaction.lower() == "открытие вклада":
                print(transfer_to)
            else:
                transfer_from = mask_account_card(item["from"])
                print(f"{transfer_from} -> {transfer_to}")
            print(f"Сумма: {amount} {currency_code}\n")
