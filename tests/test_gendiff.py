from gendiff import generate_diff


def test_json():
    with open('tests/fixtures/result.txt', 'r') as expected:
        assert generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
        ) == expected.read()


def test_yaml():
    with open('tests/fixtures/result.txt', 'r') as expected:
        assert generate_diff(
            'tests/fixtures/file1.yml',
            'tests/fixtures/file2.yml',
        ) == expected.read()


def test_nested_json():
    with open('tests/fixtures/nested_result.txt', 'r') as expected:
        assert generate_diff(
            'tests/fixtures/nested_file1.json',
            'tests/fixtures/nested_file2.json',
        ) == expected.read()
