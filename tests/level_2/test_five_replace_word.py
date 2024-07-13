import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
        "text, replace_from, replace_to, result", 
        [
            ('Сегодня прекрасная погода', 'прекрасная', 'хорошая', 'Сегодня хорошая погода'),
            ('Сегодня прекрасная погода', 'хорошая', 'прекрасная', 'Сегодня прекрасная погода'),
            ('', 'прекрасная', 'хорошая', ''), 
            ('', '', '', ''), 
        ]
)
def test_replace_word(text, replace_from, replace_to, result):
    assert replace_word(text, replace_from, replace_to) == result


def test__replace_word__one_argument_replace_and_text_not_need_type():
    text = 2345
    replace_from = 'прекрасная'
    replace_to = 234

    with pytest.raises(AttributeError):
        replace_word(text, replace_from, replace_to)


def test__replace_word__one_argument_replace_is_none():
    text = 'Сегодня прекрасная погода'
    replace_from = None
    replace_to = 'прекрасная'

    with pytest.raises(AttributeError):
        replace_word(text, replace_from, replace_to)
