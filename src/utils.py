import json


def operations_data(route=None) -> list:
    """Функция, которая загружает информацию из файла json и выводит список словарей с данными"""
    if route is None:
        return []
    else:
        with open(route, encoding="utf-8") as f:
            try:
                content = f.read()
                try:
                    data = json.loads(content)
                except json.JSONDecodeError:
                    return []
            except FileNotFoundError:
                return []
            return data
