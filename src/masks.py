def get_mask_card_number(card_number: int) -> str:
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        mask_card_number = str_card_number.replace(str_card_number[6:12], "******")
        return f"{mask_card_number[:4]} {mask_card_number[4:8]} {mask_card_number[8:12]} {mask_card_number[12:]}"
    elif len(str_card_number) == 0:
        return "нет номера карты"
    else:
        return "неверный номер карты"


def get_mask_account(account_number: int) -> str:
    """Функция, маскирующая номер карты"""
    str_account_number = str(account_number)
    if len(str_account_number) == 20:
        return f"**{str_account_number[-4:]}"
    elif len(str_account_number) == 0:
        return "нет номера счета"
    else:
        return "неверный номер счета"
