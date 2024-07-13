import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
        "items, default, result", 
        [
            ([1, 2, 3, 4], 5, 1),
            (['1', '2', '3', '4'], 5, '1'),
            ([], None, None),
            ([], 'hi', 'hi'),
            ([], 1, 1),
        ]
)
def test_first(items, default, result):
    assert first(items, default) == result


def test__first__empty_items_and_not_default():
    items = []

    with pytest.raises(AttributeError):
        first(items)
