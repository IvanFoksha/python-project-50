from .diff_builder import build_diff_tree
from .formatters.stylish import format_output
from .parser import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return format_output(diff_tree)
    else:
        raise ValueError(f'Unsupported format: {format_name}')
