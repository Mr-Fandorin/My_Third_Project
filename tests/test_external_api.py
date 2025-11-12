from unittest.mock import Mock, patch

import pytest

from src.external_api import exchange_amount


@pytest.mark.parametrize(
    "currency, expected",
    [
        ("RUB", 31957.58),
    ],
)
def test_exchange_amount(currency, expected, data_transaction):
    assert exchange_amount(data_transaction) == expected


# @patch("requests.request")
def test_exchange_amount_rate_success(data_transaction_usd):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 657709.6}

    with patch("requests.request", return_value=mock_response):
        result = exchange_amount(data_transaction_usd)
        assert result == 657709.6


def test_exchange_amount_rate_failed_request(data_transaction_usd):
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.request", return_value=mock_response):
        with pytest.raises(ValueError, match="Failed to get currency rate"):
            exchange_amount(data_transaction_usd)
