def format_node(node, depth=0):
    indent = ' ' * depth

    node_type = node['type']
    key = node.get('key')

    lines = []

    if node_type == 'nested':
        children_lines = '\n'.join(
            format_node(child, depth + 1) for child in node['children']
        )
        lines.append(f'{indent} {key}: {{\n{children_lines}\n{indent}  }}')
    elif node_type == 'changed':
        old_line = f"{indent}- {key}: {format_value(node['old_value'])}"
        new_line = f"{indent}+ {key}: {format_value(node['new_value'])}"
        lines.extend([old_line, new_line])
    elif node_type == 'added':
        line = f"{indent}+ {key}: {format_value(node['value'])}"
        lines.append(line)
    elif node_type == 'removed':
        line = f"{indent}- {key}: {format_value(node['value'])}"
        lines.append(line)
    elif node_type == 'unchanged':
        line = f"{indent}  {key}: {format_value(node['value'])}"
        lines.append(line)

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


def format_stylish(diff_tree):
    lines = [format_node(node, 0) for node in diff_tree]
    return '{\n' + '\n'.join(lines) + '\n}'
