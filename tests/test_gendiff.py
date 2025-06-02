from pathlib import Path

from hexlet_code import generate_diff
from hexlet_code.parser import parse_file

FIXTURES_PATH = Path(__file__).parent / 'test_data'


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def test_gendiff_json():
    data1 = parse_file(FIXTURES_PATH / 'file1.json')
    data2 = parse_file(FIXTURES_PATH / 'file2.json')

    result = generate_diff(data1, data2)
    expected = read_file(FIXTURES_PATH / 'expected_result.txt').strip()

    assert result.strip() == expected


def test_gendiff_yaml():
    data1 = parse_file(FIXTURES_PATH / 'file1.yml')
    data2 = parse_file(FIXTURES_PATH / 'file2.yaml')

    result = generate_diff(data1, data2)
    expected = read_file(FIXTURES_PATH / 'expected_result.txt').strip()

    assert result.strip() == expected
