import xmltodict
import sys
import json
import yaml


def parse_args():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def read_json(file_path):
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Invalid JSON file")
            sys.exit(1)


def write_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def read_yaml(file_path):
    with open(file_path, "r") as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError:
            print("Invalid YAML file")
            sys.exit(1)


def write_yaml(file_path, data):
    with open(file_path, "w") as file:
        yaml.safe_dump(data, file)


def read_xml(file_path):
    with open(file_path, "r") as file:
        try:
            data = xmltodict.parse(file.read())
            return data
        except Exception as e:
            print("Invalid XML file:", e)
            sys.exit(1)


if __name__ == "__main__":
    pathFile1, pathFile2 = parse_args()
    if pathFile1.endswith(".json"):
        data = read_json(pathFile1)
    elif pathFile1.endswith(".yml") or pathFile1.endswith(".yaml"):
        data = read_yaml(pathFile1)
    elif pathFile1.endswith(".xml"):
        data = read_xml(pathFile1)
    if pathFile2.endswith(".json"):
        write_json(pathFile2, data)
    elif pathFile2.endswith(".yml") or pathFile2.endswith(".yaml"):
        write_yaml(pathFile2, data)
