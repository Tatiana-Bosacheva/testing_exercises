import pytest

from functions.level_1.five_title import change_copy_item

@pytest.mark.parametrize(
        "text, number, result", 
        [
            ('Заголовок', 5, 'Заголовок'),
            ('100 самых интересных мест в России', None, 'Copy of 100 самых интересных мест в России'),
            ('Copy of 100 самых интересных мест в России (3)', None, 'Copy of 100 самых интересных мест в России (4)'),
            ('Copy of 100 самых интересных мест в России', None, 'Copy of 100 самых интересных мест в России (2)'),
        ]
)
def test_change_copy_item(text, number, result):
    if number:
        assert change_copy_item(text, number) == result
    else:
        assert change_copy_item(text) == result
