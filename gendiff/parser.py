import json
import yaml


def booleans_to_string(value):
    if type(value) is bool:
        return str(value).lower()
    return value


def parse_json(text):
    data = json.load(text)
    return {key: booleans_to_string(val) for key, val in data.items()}


def parse_yaml(text):
    data = yaml.load(text, Loader=yaml.Loader)
    return {key: booleans_to_string(val) for key, val in data.items()}


def parse(filepath):
    extension = filepath.split('.')[-1]

    if extension == 'json':
        with open(filepath, 'r') as config:
            return parse_json(config)
    if extension in ('yml', 'yaml'):
        with open(filepath, 'r') as config:
            return parse_yaml(config)
