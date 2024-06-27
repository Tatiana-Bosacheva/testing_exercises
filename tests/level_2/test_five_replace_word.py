import pytest

from functions.level_2.five_replace_word import replace_word


def test__replace_word__change_words():
    text = 'Сегодня прекрасная погода'
    replace_from = 'прекрасная'
    replace_to = 'хорошая'

    res = replace_word(text, replace_from, replace_to)

    assert res == 'Сегодня хорошая погода'


def test__replace_word__no_change_words():
    text = 'Сегодня прекрасная погода'
    replace_from = 'хорошая'
    replace_to = 'прекрасная'

    res = replace_word(text, replace_from, replace_to)

    assert res == 'Сегодня прекрасная погода'


def test__replace_word__text_is_empty_string():
    text = ''
    replace_from = 'прекрасная'
    replace_to = 'хорошая'

    res = replace_word(text, replace_from, replace_to)

    assert res == ''


def test__replace_word__all_arguments_is_empty_string():
    text = ''
    replace_from = ''
    replace_to = ''

    res = replace_word(text, replace_from, replace_to)

    assert res == ''


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
