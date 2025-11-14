import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def operations_data(route=None) -> list:
    """Функция, которая загружает информацию из файла json и выводит список словарей с данными"""
    if route is None:
        logger.info("Нет адреса файла")
        return []
    else:
        try:
            logger.info(f"Открываем файл JSON по адресу {route}")
            with open(route, encoding="utf-8") as f:
                content = f.read()
                try:
                    logger.info("Преобразуем JSON-строку в объект Python")
                    data = json.loads(content)
                except json.JSONDecodeError:
                    logger.error("Неверный формат файла")
                    return []
        except FileNotFoundError:
            logger.error("Файл JSON не найден")
            return []
        return data
