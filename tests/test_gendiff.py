from pathlib import Path
from hexlet_code import generate_diff


FIXTURES_PATH = Path(__file__).parent / 'test_data'


def read_file(file_name):
    with open(FIXTURES_PATH / file_name, 'r') as f:
        return f.read()


def test_gendiff_json():
    result = generate_diff(
        FIXTURES_PATH / 'file1.json',
        FIXTURES_PATH / 'file2.json'
    )
    expected = read_file('expected_result.txt').strip()
    assert result.strip() == expected
