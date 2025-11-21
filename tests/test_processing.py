import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.mark.parametrize(
    "action, expected",
    [
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 615064000, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
            ],
        ),
        ("SOMETHING", "нет данных"),
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(list_of_users, action, expected):
    assert filter_by_state(list_of_users, action) == expected


@pytest.mark.parametrize(
    "sorting_parameter, expected",
    [
        (
            " ",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 615064000, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 615064000, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 615064000, "state": "CANCELED", "date": "2018:10:14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(list_of_users, sorting_parameter, expected):
    assert sort_by_date(list_of_users, sorting_parameter) == expected


@pytest.mark.parametrize(
    "search_word, expected",
    [
        (
            "организации",
            [
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "amount": "9824.07",
                    "currency_code": "USD",
                    "currency_name": "USD",
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
        (
            "счет",
            [
                {
                    "date": "2019-03-23T01:09:46.296404",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "id": 873106923,
                    "amount": "43318.34",
                    "currency_code": "RUB",
                    "currency_name": "руб.",
                    "state": "EXECUTED",
                    "to": "Счет 74489636417521191160",
                }
            ],
        ),
    ],
)
def test_process_bank_search(transactions, search_word, expected):
    assert process_bank_search(transactions, search_word) == expected


@pytest.mark.parametrize(
    "list_category, expected",
    [
        (
            ["Перевод организации", "Перевод со счета на счет"],
            {"Перевод организации": 1, "Перевод со счета на счет": 1},
        ),
    ],
)
def test_process_bank_operations(transactions, list_category, expected):
    assert process_bank_operations(transactions, list_category) == expected
