import json

def operations_data(route=None) -> list:
    "Функция, которая загружает информацию из файла json и выводит список словарей с данными"
    if route is None:
        return []
    else:
        with open(route, encoding='utf-8') as f:
            content = f.read()
            if not content:
                return []
            data = json.loads(content)
            if type(data) != list:
                return []
            return data


