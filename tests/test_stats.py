import pytest
from src.stats import get_char_count, get_num_words, sort_char_count

def test_get_num_words():
    assert get_num_words("Hello World") == 2
    assert get_num_words("This      is  three") == 3

def test_get_char_counts():
    counts = get_char_count("aAbB ")
    assert counts["a"] == 2
    assert counts["b"] == 2
    assert counts[" "] == 1

def test_sort_char_count():
    raw = {'a': 5, 'b': 1, 'c': 3}
    sorted_list = sort_char_count(raw)
    expected = [{'char': 'a', 'num': 5}, {'char': 'c', 'num': 3}, {'char': 'b', 'num': 1}]
    assert sorted_list == expected
