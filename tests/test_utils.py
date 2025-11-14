import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import operations_data


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 441945886, "state": "EXECUTED"}]))
def test_operations_data(mock_file):
    assert operations_data("..data/operations.json") == [{"id": 441945886, "state": "EXECUTED"}]
    mock_file.assert_called_once_with("..data/operations.json", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_operations_data_2(mock_file):
    assert operations_data("..data/operations.json") == []
    mock_file.assert_called_once_with("..data/operations.json", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_operations_data_3(mock_file):
    assert operations_data("..data/operations.json") == []
    mock_file.assert_called_once_with("..data/operations.json", encoding="utf-8")


@pytest.mark.parametrize("value, expected", [(None, [])])
def test_operations_data_2(value, expected):
    assert operations_data(value) == expected
