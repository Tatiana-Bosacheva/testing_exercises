import pytest

from functions.level_1.three_url_builder import build_url

@pytest.mark.parametrize(
        "domain, page, parametres, result", 
        [
            ('example.com', 'articles', {'code': '1'}, 'example.com/articles?code=1'),
            ('example.com', 'articles', None, 'example.com/articles'),
        ]
)
def test_build_url(domain, page, parametres, result):
    assert build_url(domain, page, parametres) == result
