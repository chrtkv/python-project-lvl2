from gendiff.parser import parse


def generate_diff(path1, path2, format='stylish'):
    """Generate diff of two files

    Args:
        path1 (str): Path to the first file
        path2 (str): Path to the second file
        format (str): Output format

    Returns:
        string: Difference between two files in selected format
    """

    file1 = parse(path1)
    file2 = parse(path2)

    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    diff = []

    for key in keys1 | keys2:
        if key in keys1 and key in keys2:
            if file1[key] == file2[key]:
                diff.append({
                    "key": key,
                    "value1": file1[key],
                    "value2": file2[key],
                    "status": "unchanged"
                })
            else:
                diff.append({
                    "key": key,
                    "value1": file1[key],
                    "value2": file2[key],
                    "status": "updated",
                })

        elif key in keys1:
            diff.append({
                "key": key,
                "value1": file1[key],
                "value2": None,
                "status": "removed",
            })

        elif key in keys2:
            diff.append({
                "key": key,
                "value1": None,
                "value2": file2[key],
                "status": "added",
            })

    return diff
