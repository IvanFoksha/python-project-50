import json

from .stylish import format_value


def format_json(diff_tree):
    return json.dumps(diff_tree, indent=2,
                      default=format_value, sort_keys=False)
