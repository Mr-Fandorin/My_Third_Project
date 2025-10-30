import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("", "нет номера карты"),
        ("700079228960636", "неверный номер карты"),
        ("700079228960636100", "неверный номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("", "нет номера счета"),
        ("736541084301358743", "неверный номер счета"),
        ("7365410843013587430500", "неверный номер счета"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
