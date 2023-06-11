import pytest

from functions.level_1_5.five_replace_word import replace_word

def test__replace_word__text_contains_a_word_from_replace_from():
    text = 'One TwO Three Four'
    replace_from = 'tWo'
    replace_to = 'ZerO'

    result = replace_word(text, replace_from, replace_to)

    assert result == 'One ZerO Three Four'


def test__replace_word__text_not_contains_a_word_from_replace_from():
    text = 'One TwO Three Four'
    replace_from = 'five'
    replace_to = 'ZerO'

    result = replace_word(text, replace_from, replace_to)

    assert result == 'One TwO Three Four'


def test__replace_word__text_contains_commas():
    text = 'One TwO, Three Four'
    replace_from = 'tWo'
    replace_to = 'ZerO'

    result = replace_word(text, replace_from, replace_to)

    assert result == 'One TwO, Three Four'