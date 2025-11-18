import csv
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.transactions import reader_csv_transactions, reader_excel_transaction


@patch("csv.DictReader")
def test_reader_csv_transactions(mock_reader):
    with patch("builtins.open", mock_open()) as mocked_open:
        mock_reader.return_value = [{"id": 441945886, "state": "EXECUTED"}]
        result = reader_csv_transactions("list_data")
        expected = [{"id": 441945886, "state": "EXECUTED"}]
        assert result == expected


def test_reader_excel_transaction():
    df = pd.DataFrame({"name": ["Tom", "Mike"], "age": ["35", "45"]})
    with patch("pandas.read_excel") as mocked_read:
        mocked_read.return_value = df
        result = reader_excel_transaction("list_data")
        expected = [{"age": "35", "name": "Tom"}, {"age": "45", "name": "Mike"}]
        assert result == expected
