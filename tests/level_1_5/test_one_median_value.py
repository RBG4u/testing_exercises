import pytest

from functions.level_1_5.one_median import get_median_value


def test__get_median_value__empty_list():
    assert get_median_value([]) == None


def test__get_median_value__even_list():
    assert get_median_value([4, 6, 1, 12, 7, 23]) == 15


def test__get_median_value__odd_list():
    assert get_median_value([4, 6, 1, 12, 7]) == 12


def test__get_median_value__len_one_two_four_list():
    with pytest.raises(IndexError):
        get_median_value([4])
    with pytest.raises(IndexError):
        get_median_value([4, 6])
    with pytest.raises(IndexError):
        get_median_value([4, 6, 1, 12])
        