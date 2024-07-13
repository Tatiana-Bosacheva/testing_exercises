import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
        "text, good_words, bad_words, result", 
        [
            ("Сегодня прекрасная погода", {'прекрасная', 'хорошая'}, {}, 'GOOD'),
            ("Этот фильм ужасен", {}, {"ужасен"}, "BAD"),
            ("Фильм хороший но немного затянутый", {"хороший"}, {"затянутый"}, None), 
            ("", {}, {}, None), 
            ("Это просто текст", {}, {}, None),
        ]
)
def test_check_tweet_sentiment(text, good_words, bad_words, result):
    assert check_tweet_sentiment(text, good_words, bad_words) == result


def test__check_tweet_sentiment__text_is_none():
    text = None
    good_words = {}
    bad_words = {}

    with pytest.raises(AttributeError):
        check_tweet_sentiment(text, good_words, bad_words)
