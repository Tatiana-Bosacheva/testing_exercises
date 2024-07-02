from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__true():
    url = 'https://github.com/Tatiana-Bosacheva/typing_challenges/pull/2'

    res = is_github_pull_request_url(url)

    assert res is True


def test__is_github_pull_request_url__len_not_seven():
    url = 'https:/github.com/Tatiana-Bosacheva/typing_challenges/pull/2'

    res = is_github_pull_request_url(url)

    assert res is False


def test__is_github_pull_request_url__not_github():
    url = 'https://gitlab.com/Tatiana-Bosacheva/typing_challenges/pull/2'

    res = is_github_pull_request_url(url)

    assert res is False


def test__is_github_pull_request_url__not_pull():
    url = 'https://github.com/Tatiana-Bosacheva/nfa_app/tree/main'

    res = is_github_pull_request_url(url)

    assert res is False


def test__is_github_pull_request_url__incorrect_url():
    url = "http://example.com"

    res = is_github_pull_request_url(url)

    assert res is False
