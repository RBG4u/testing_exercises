import pytest

from functions.level_1_5.three_first import first, NOT_SET

def test__first__is_list():
    assert first([2, 5, 6], 3) == 2


def test__first__not_list():
    assert first([], 3) == 3


def test__first__not_list_and_not_set_default():
    with pytest.raises(AttributeError):
        first([], NOT_SET)
        