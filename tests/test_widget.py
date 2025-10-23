import pytest


from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('value, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('', 'нет данных'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('5999414228426353', 'недостаточно данных'),
    ('MasterCard 715830073472', 'неверный номер карты'),
    ('Visa Platinum 89909221136652298888', 'неверный номер карты'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Счет 64686473678894779', 'неверный номер счета'),
    ('Счет 646864736788947795899999', 'неверный номер счета')
])

def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

