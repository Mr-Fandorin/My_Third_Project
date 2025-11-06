from typing import Union


def filter_by_state(list_of_user_dates: list[dict], state: str = "EXECUTED") -> Union[str, list[dict]]:
    """Функция, фильтрующая словари по нужному ключу"""
    new_list_of_users = []
    for item in list_of_user_dates:
        for value in item.values():
            if value == state:
                new_list_of_users.append(item)
    if new_list_of_users == []:
        return "нет данных"
    else:
        return new_list_of_users


def sort_by_date(list_of_user_dates: list[dict], sorting_type: bool = True) -> list[dict]:
    """Функция, сортирующая словари по нужному ключу"""
    sorted_list_of_users = sorted(list_of_user_dates, key=lambda dict_user: dict_user["date"], reverse=sorting_type)
    return sorted_list_of_users
