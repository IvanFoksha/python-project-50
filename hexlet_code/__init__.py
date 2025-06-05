from .diff_builder import build_diff_tree
from .formatters.stylish import format_stylish
from .parser import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        inner = format_stylish(diff_tree)
        return '{\n' + inner + '\n}'
    else:
        raise ValueError(f'Unsupported format: {format_name}')


def generate_diff_from_data(data1, data2, format_name='stylish'):
    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        inner = format_stylish(diff_tree, depth=1)
        return '{\n' + inner + '\n}'
    else:
        raise ValueError(f'Unsupported format: {format_name}')
