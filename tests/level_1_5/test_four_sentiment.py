import pytest

from functions.level_1_5.four_sentiment import check_tweet_sentiment

def test__check_tweet_sentiment__good():
    text = 'good bad pizza'
    good_words = {'good', 'pizza'}
    bad_words = {'bad', 'cringe'}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'GOOD'


def test__check_tweet_sentiment__bad():
    text = 'good bad pizza'
    good_words = {'good', 'nice'}
    bad_words = {'bad', 'pizza'}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == 'BAD'


def test__check_tweet_sentiment__neutral():
    text = 'good bad pizza'
    good_words = {'good', 'nice'}
    bad_words = {'bad', 'cringe'}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None


def test__check_tweet_sentiment__text_with_commas():
    text = 'good, bad nice'
    good_words = {'good', 'nice'}
    bad_words = {'bad', 'cringe'}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None


def test__check_tweet_sentiment__no_text():
    text = ''
    good_words = {'good', 'nice'}
    bad_words = {'bad', 'cringe'}

    result = check_tweet_sentiment(text, good_words, bad_words)

    assert result == None