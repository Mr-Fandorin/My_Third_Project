import os
from typing import Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def exchange_amount(transaction: dict) -> Union[float, str]:
    """Функция, которая производит конвертацию суммы транзакции в рубли"""
    amount = float(transaction["operationAmount"]["amount"])
    from_currency = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    if from_currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"

        payload = {"amount": amount, "from_currency": from_currency, "to": to}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, params=payload)
        if response.status_code != 200:
            raise ValueError("Failed to get currency rate")
        status_code = response.status_code
        result = response.json()["result"]
        if not from_currency:
            raise ValueError(f"No data for currency {from_currency}")
        return result
