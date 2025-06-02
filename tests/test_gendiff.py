import json
from pathlib import Path

from hexlet_code import generate_diff

FIXTURES_PATH = Path(__file__).parent / 'test_data'


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def test_gendiff_json():
    data1 = read_json(FIXTURES_PATH / 'file1.json')
    data2 = read_json(FIXTURES_PATH / 'file2.json')

    result = generate_diff(data1, data2)
    expected = read_file(FIXTURES_PATH / 'expected_result.txt').strip()

    assert result.strip() == expected
