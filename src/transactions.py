import csv

import pandas as pd


def reader_csv_transactions(file_csv):
    """Функция, которая загружает информацию из файла csv и выводит список словарей с данными"""
    with open(file_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        list_transactions = []
        for row in reader:
            list_transactions.append(row)
    return list_transactions


def reader_excel_transaction(file_excel):
    """Функция, которая загружает информацию из файла excel и выводит список словарей с данными"""
    excel_reader = pd.read_excel(file_excel)
    list_excel_transactions = excel_reader.to_dict(orient="records")
    return list_excel_transactions
