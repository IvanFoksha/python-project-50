def format_stylish(diff_tree, depth=0):
    indent = '  ' * depth

    lines = []

    for node in diff_tree:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children_lines = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {{")
            lines.append(children_lines)
            lines.append(f"{indent}  }}")

        elif node_type == 'changed':
            lines.append(f"{indent}- {key}: {format_value(node['old_value'])}")
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'])}")

        elif node_type == 'added':
            lines.append(f"{indent}+ {key}: {format_value(node['value'])}")

        elif node_type == 'removed':
            lines.append(f"{indent}- {key}: {format_value(node['value'])}")

        elif node_type == 'unchanged':
            lines.append(f"{indent}  {key}: {format_value(node['value'])}")

    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict):
        return '{ ... }'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)
