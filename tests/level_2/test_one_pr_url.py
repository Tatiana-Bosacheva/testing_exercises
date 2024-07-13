import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
        "link, result", 
        [
            ('https://github.com/Tatiana-Bosacheva/typing_challenges/pull/2', True),
            ('https:/github.com/Tatiana-Bosacheva/typing_challenges/pull/2', False),
            ('https://gitlab.com/Tatiana-Bosacheva/typing_challenges/pull/2', False),
            ('https://github.com/Tatiana-Bosacheva/nfa_app/tree/main', False),
            ("http://example.com", False),
        ]
)
def test_is_github_pull_request_url(link, result):
    assert is_github_pull_request_url(link) is result
