from functions.level_1.one_gender import genderalize


def test_genderalize():
    verb_male = 'M'
    verb_female = 'F'
    test_cases = [
        ('male', 'M'),
        ('female', 'F'),
    ]
    for gender, expected_result in test_cases:
        assert genderalize(verb_male, verb_female, gender) == expected_result
