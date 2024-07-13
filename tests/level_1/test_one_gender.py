import pytest
from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
        "male_verb, female_verb, gender, result", 
        [
            ('делал', 'делала', 'male', 'делал'),
            ('делал', 'делала', 'female', 'делала'),
        ]
)
def test_genderalize(male_verb, female_verb, gender, result):
    assert genderalize(male_verb, female_verb, gender) == result
