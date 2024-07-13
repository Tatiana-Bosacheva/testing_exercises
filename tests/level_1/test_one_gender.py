from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('делал', 'делала', 'male') == 'делал'
    assert genderalize('делал', 'делала', 'female') == 'делала'
