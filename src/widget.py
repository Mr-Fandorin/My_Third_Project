import re

import masks
# from . import masks


def mask_account_card(card_account_num: str) -> str:
    """Функция маскирующая номер счета или карты"""
    if re.search("[а-яА-Я]", card_account_num):
        if len(card_account_num) == 25:
            mask_account_num = masks.get_mask_account(int(card_account_num[-20:]))
            return f"{card_account_num[:-20]}{mask_account_num}"
        else:
            return 'неверный номер счета'
    elif re.search("[a-zA-Z]", card_account_num):
        list_card_num = card_account_num.split(' ')
        if len(list_card_num[-1]) == 16:
            mask_card_num = masks.get_mask_card_number(int(card_account_num[-17:]))
            return f"{card_account_num[:-17]} {mask_card_num}"
        else:
            return 'неверный номер карты'
    elif len(card_account_num) == 0:
        return 'нет данных'
    else:
        return 'недостаточно данных'


def get_date(full_date: str) -> str:
    """Функция упрощающая вид даты"""
    part_full_date = full_date[:10]
    split_date = part_full_date.split("-")

    rev_list_date = split_date[-1:-4:-1]
    short_date = ".".join(rev_list_date)
    return short_date
