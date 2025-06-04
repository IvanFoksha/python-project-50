import argparse

from ..__init__ import generate_diff

# def read_file(file_path):

#     file_ext = Path(file_path).suffix.lower()

#     if file_ext == '.json':
#         with open(file_path, 'r') as f:
#             return json.load(f)
#     else:
#         raise ValueError(f'Unsupported file format: {file_ext}')


# def format_value(value):
#     if isinstance(value, bool):
#         return 'true' if value else 'false'
#     elif value is None:
#         return 'null'
#     else:
#         return str(value)


# def generate_diff(data1, data2):
#     keys = sorted(set(data1.keys()) | set(data2.keys()))
#     lines = []

#     for key in keys:
#         val1 = data1.get(key)
#         val2 = data2.get(key)

#         if key in data1 and key not in data2:
#             lines.append(f'- {key}: {format_value(val1)}')
#         elif key in data2 and key not in data1:
#             lines.append(f'+ {key}: {format_value(val2)}')
#         elif val1 != val2:
#             lines.append(f'- {key}: {format_value(val1)}')
#             lines.append(f'+ {key}: {format_value(val2)}')
#         else:
#             lines.append(f'  {key}: {format_value(val1)}')

#     return '{\n' + '\n'.join(f'  {line}' for line in lines) + '\n}'


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

    print(generate_diff(args.first_file,
                        args.second_file,
                        format_name=args.format))


if __name__ == '__main__':
    main()
