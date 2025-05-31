import argparse
import json
from pathlib import Path


def read_file(file_path):

    file_ext = Path(file_path).suffix.lower()

    if file_ext == '.json':
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        raise ValueError(f'Unsupported file format: {file_ext}')


def generate_diff(data1, data2):
    keys = sorted(set(data1.keys())) | set(data2.keys())
    lines = []

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key in data1 and key not in data2:
            lines.append(f'- {key}: {val1}')
        elif key in data2 and key not in data1:
            lines.append(f'+ {key}: {val2}')
        elif val2 != val2:
            lines.append(f'- {key}: {val1}')
            lines.append(f'+ {key}: {val2}')
        else:
            lines.append(f'  {key}: {val1}')

    return '{\n' + '\n'.join(f'  {line}' for line in lines) + '\n}'


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

    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)

    print(generate_diff(data1, data2))


if __name__ == '__main__':
    main()
