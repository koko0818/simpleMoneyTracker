from project import track, category, balance
from unittest import mock
from unittest import TestCase
import pytest

categories = {
    "salary": 0.0,
    "other income": 0.0,
    "food": 0.0,
    "rent/utilities": 0.0,
    "transportation": 0.0,
    "hobby": 0.0
}

@mock.patch('builtins.input', create=True)
def test_track_okay(mock_input):
    mock_input.side_effect = ["food", "10"]
    result = track(categories)
    assert result["food"] == 10

@mock.patch('builtins.input', create=True)
def test_track_key_error(mocked_input):
    mocked_input.side_effect = ["pet", 10]
    with pytest.raises(KeyError):
        track(categories)

@mock.patch('builtins.input', create=True)
def test_track_value_error(mocked_input):
    mocked_input.side_effect = ["food", "hello"]
    with pytest.raises(ValueError):
        track(categories)

@mock.patch('builtins.input', create=True)
def test_category_okay(mocked_input):
    mocked_input.side_effect = ["Y", "pet"]
    result = category(categories)
    assert result["pet"] == 0

@mock.patch('builtins.input', create=True)
def test_category_okay(mocked_input):
    mocked_input.side_effect = ["N"]
    result = category(categories)
    orig_num_categories = len(result)
    assert len(categories) == orig_num_categories

@mock.patch('builtins.input', create=True)
def test_category_attribute_error(mocked_input):
    mocked_input.side_effect = [0]
    with pytest.raises(AttributeError):
        category(categories)

@mock.patch('builtins.input', create=True)
def test_category_value_error(mocked_input):
    mocked_input.side_effect = ["hello"]
    with pytest.raises(ValueError):
        category(categories)

def test_balance():
    assert balance(categories) == 10
    new_categories = {
        "salary": 1000.0,
        "other income": 15.5,
        "food": 0.0,
        "rent/utilities": -10.20,
        "transportation": -5.50,
        "hobby": 0.0
    }
    result = balance(new_categories)
    assert result == (1000+15.5-10.20-5.50)