import pytest
from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    #Test 1
    title = 'Title'
    expected_result = 'Copy of Title'
    assert change_copy_item(title) == expected_result

    #Test 2
    title = 'Copy of Title'
    expected_result = 'Copy of Title (2)'
    assert change_copy_item(title) == expected_result

    #Test 3
    title = 'Copy of Title (2)'
    expected_result = 'Copy of Title (3)'
    assert change_copy_item(title) == expected_result

    #Test 4
    title = 'TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle'
    expected_result = 'TitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitleTitle'
    assert change_copy_item(title) == expected_result
