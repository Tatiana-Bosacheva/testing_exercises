import pytest

from functions.level_2.three_first import first


def test__first__true():
    items = [1, 2, 3, 4]
    default = 5

    res = first(items, default)

    assert res == 1


def test__first__items_not_int():
    items = ['1', '2', '3', '4']
    default = 5

    res = first(items, default)

    assert res == '1'


def test__first__empty_items_and_default_is_none():
    items = []
    default = None

    res = first(items, default)

    assert res == None


def test__first__empty_items_and_default_is_str():
    items = []
    default = 'hi'

    res = first(items, default)

    assert res == 'hi'


def test__first__empty_items_and_default_is_int():
    items = []
    default = 1

    res = first(items, default)

    assert res == 1


def test__first__empty_items_and_not_default():
    items = []

    with pytest.raises(AttributeError):
        first(items)
