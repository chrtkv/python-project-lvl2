from gendiff.parser import parse


def generate_diff(path1, path2):
    """Generate diff of two files

    Args:
        file1 (str): Path to the first file
        file2 (str): Path to the second file

    Returns:
        string: Difference between two files
    """

    file1 = parse(path1)
    file2 = parse(path2)

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
