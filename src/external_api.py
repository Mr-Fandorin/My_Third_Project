import os
from dotenv import load_dotenv

import requests


load_dotenv()
API_KEY = os.getenv("API_KEY")

data = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

def exchange_amount(transaction):
    amount = float(transaction["operationAmount"]["amount"])
    from_currency = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    if from_currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"

        payload = {
            "amount": amount,
            "from_currency": from_currency,
            "to": to
        }
        headers= {
          "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, params=payload)

        status_code = response.status_code
        result = response.json()['result']

        return result

print(exchange_amount(data))

