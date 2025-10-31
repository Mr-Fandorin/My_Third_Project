import pytest

from src.generators import filter_by_currency
from tests.conftest import transactions

@pytest.mark.parametrize(
    "currency, expected",
    [
        (
                'USD',
                {'date': '2018-06-30T02:08:58.425572',
                 'description': 'Перевод организации',
                 'from': 'Счет 75106830613657916952',
                 'id': 939719570,
                 'operationAmount': {'amount': '9824.07',
                                     'currency': {'code': 'USD', 'name': 'USD'}},
                 'state': 'EXECUTED',
                 'to': 'Счет 11776614605963066702'}
        ),
        (
                'RUB',
                {'date': '2019-03-23T01:09:46.296404',
                 'description': 'Перевод со счета на счет',
                 'from': 'Счет 44812258784861134719',
                 'id': 873106923,
                 'operationAmount': {'amount': '43318.34',
                                     'currency': {'code': 'RUB', 'name': 'руб.'}},
                 'state': 'EXECUTED',
                 'to': 'Счет 74489636417521191160'}
        ),
        (
                'EURO', 'Нет данных'),
        (
                '', 'Нет данных')
    ]
)


def test_filter_by_currency(currency, expected, transactions):
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == expected
    # assert next(generator) == expected
    # assert next(generator) == expected
    # assert next(generator) == expected

