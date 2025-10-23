import pytest

from src.processing import filter_by_state, sort_by_date

from tests.conftest import list_of_users


@pytest.mark.parametrize('action, expected', [
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 615064000, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'}
    ]),
    ('SOMETHING', 'нет данных'),
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ])
])

def test_filter_by_state(list_of_users, action, expected):
    assert filter_by_state(list_of_users, action) == expected



@pytest.mark.parametrize('sorting_parameter, expected', [
    (' ', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 615064000, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 615064000, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 615064000, 'state': 'CANCELED', 'date': '2018:10:14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
])


def test_sort_by_date(list_of_users, sorting_parameter, expected):
    assert sort_by_date(list_of_users, sorting_parameter) == expected