import json

def operations_data(route=None):
    "Функция, котороая загружает информацию из файла json и выводит список словарей с данными"
    if route is None:
        return []
    else:
        with open(route, encoding='utf-8') as f:
            data = json.load(f)
            if data == [] or type(data) != list or data is None:
                return []
            else:
                return data


