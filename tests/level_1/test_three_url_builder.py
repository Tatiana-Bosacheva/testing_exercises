from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('example.com', 'articles', {'code': '1'}) == 'example.com/articles?code=1'
    assert build_url('example.com', 'articles') == 'example.com/articles'
