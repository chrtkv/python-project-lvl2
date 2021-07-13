import json


def prepare_json(path1, path2):
    with open(path1, 'r') as file1, open(path2, 'r') as file2:
        file1 = json.load(file1)
        file2 = json.load(file2)

    def convert_booleans(value):
        if type(value) is bool:
            return str(value).lower()
        return value

    return [
        {key: convert_booleans(val) for key, val in file1.items()},
        {key: convert_booleans(val) for key, val in file2.items()},
    ]


def generate_diff(path1, path2):
    """Generate diff of two files

    Args:
        file1 (dict): First file content
        file2 (dict): Second file content
        format: File format

    Returns:
        string: Difference between two files
    """

    file1, file2 = prepare_json(path1, path2)

    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    result = []

    for key in keys1 | keys2:
        if key in keys1 and key in keys2:
            if file1[key] == file2[key]:
                result.append(f"    {key}: {file1[key]}")
            else:
                result.append(f"  - {key}: {file1[key]}")
                result.append(f"  + {key}: {file2[key]}")
        elif key in keys1:
            result.append(f"  - {key}: {file1[key]}")
        elif key in keys2:
            result.append(f"  + {key}: {file2[key]}")

    result.sort(key=lambda line: (line.split(':')[0][4:]))
    return "{{\n{}\n}}".format('\n'.join(result))
