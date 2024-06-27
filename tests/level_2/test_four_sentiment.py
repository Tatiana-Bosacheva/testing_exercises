import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__good_more_than_bad():
    text = "Сегодня прекрасная погода"
    good_words = {'прекрасная', 'хорошая'}
    bad_words = {}

    res = check_tweet_sentiment(text, good_words, bad_words)

    assert res == 'GOOD'


def test__check_tweet_sentiment__bad_more_than_good():
    text = "Этот фильм ужасен"
    good_words = {}
    bad_words = {"ужасен"}

    res = check_tweet_sentiment(text, good_words, bad_words)

    assert res == "BAD"


def test__check_tweet_sentiment__bad_equals_good():
    text = "Фильм хороший но немного затянутый"
    good_words = {"хороший"}
    bad_words = {"затянутый"}

    res = check_tweet_sentiment(text, good_words, bad_words)

    assert res == None


def test__check_tweet_sentiment__text_is_empty_string():
    text = ""
    good_words = {}
    bad_words = {}

    res = check_tweet_sentiment(text, good_words, bad_words)

    assert res == None


def test__check_tweet_sentiment__no_bad_and_good_words():
    text = "Это просто текст"
    good_words = {}
    bad_words = {}

    res = check_tweet_sentiment(text, good_words, bad_words)

    assert res == None


def test__check_tweet_sentiment__text_is_none():
    text = None
    good_words = {}
    bad_words = {}

    with pytest.raises(AttributeError):
        check_tweet_sentiment(text, good_words, bad_words)
