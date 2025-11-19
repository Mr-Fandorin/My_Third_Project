import logging
import os

PATH_TO_FILE_MASK = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "logs", "mask.log")

logger = logging.getLogger("mask")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_FILE_MASK, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    logger.debug(f"Значение переменной str_card_number: {str_card_number}")
    if len(str_card_number) == 16:
        logger.info("Маскируем часть номера карты звездочками")
        mask_card_number = str_card_number.replace(str_card_number[6:12], "******")
        logger.debug(f"Значение переменной mask_card_number: {mask_card_number}")
        return f"{mask_card_number[:4]} {mask_card_number[4:8]} {mask_card_number[8:12]} {mask_card_number[12:]}"
    elif len(str_card_number) == 0:
        logger.info("Нет номера карты")
        return "нет номера карты"
    else:
        logger.info("Неверный номер карты")
        return "неверный номер карты"


def get_mask_account(account_number: int) -> str:
    """Функция, маскирующая номер карты"""
    str_account_number = str(account_number)
    logger.debug(f"Значение переменной str_account_number: {str_account_number}")
    if len(str_account_number) == 20:
        logger.info("Маскируем часть номера счета звездочками")
        return f"**{str_account_number[-4:]}"
    elif len(str_account_number) == 0:
        logger.info("Нет номера счета")
        return "нет номера счета"
    else:
        logger.info("Неверный номер счета")
        return "неверный номер счета"
