import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file',
                        help='Path to the first configuration file')
    parser.add_argument('second_file',
                        help='Path to the second configuration file')
    parser.add_argument('-f', '--format', metavar='FORMAT', default='stylish',
                        help='set format of output (default: stylish)')

    args = parser.parse_args()
    print('Gendiff is ready to rock! Use -h for help')


def read_file(file_path):
    file_ext = Path(file_path).suffix.lower()

    if file_ext == '.json':
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        raise ValueError(f'Unsupported file format: {file_ext}')


if __name__ == '__main__':
    main()
