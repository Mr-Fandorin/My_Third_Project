import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
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


def test_transaction_descriptions(transactions):
    expected_descriptions = [
        'Перевод организации',
        'Перевод со счета на счет'
    ]

    generator = transaction_descriptions(transactions)
    for expected, generated in zip(expected_descriptions, generator):
        assert generated == expected


def test_transaction_descriptions(dates):
    expected_descriptions = 'Нет данных'

    generator = transaction_descriptions(dates)
    assert next(generator) == expected_descriptions


# @pytest.mark.parametrize('num_start, num_finish, expected',
#                          [('1', '5',
#                            ['0000 0000 0000 0001', '0000 0000 0000 0002',
#                             '0000 0000 0000 0003', '0000 0000 0000 0004',
#                             '0000 0000 0000 0005']
#                            )
#                           ]
#                          )
#
# def test_card_number_generator(num_start, num_finish, expected):
#     generator = card_number_generator(num_start, num_finish)
#     for card in generator:
#         assert next(generator) == expected
#         # assert next(generator) == expected

def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'
    assert next(generator) == '0000 0000 0000 0003'
    assert next(generator) == '0000 0000 0000 0004'
    assert next(generator) == '0000 0000 0000 0005'

def test_card_number_generator():
    generator = card_number_generator(9999999999999996, 9999999999999999)
    assert next(generator) == '9999 9999 9999 9996'
    assert next(generator) == '9999 9999 9999 9997'
    assert next(generator) == '9999 9999 9999 9998'
    assert next(generator) == '9999 9999 9999 9999'

def test_card_number_generator():
    generator = card_number_generator(9999999999999999, 10000000000000000)
    assert next(generator) == '9999 9999 9999 9999'
    assert next(generator) == 'неверный номер карты'
