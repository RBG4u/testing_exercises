from functions.level_1.three_url_builder import build_url


def test_build_url():
    host_name = "HOST"
    relative_url = 'URL'
    test_cases = [
        ({'param1': 'value1', 'param2': 'value2'}, 'HOST/URL?param1=value1&param2=value2'),
        ({'param1': 'value1'}, 'HOST/URL?param1=value1'),
        ({}, 'HOST/URL')
    ]
    for params, expected_result in test_cases:
        assert build_url(host_name, relative_url, params) == expected_result
