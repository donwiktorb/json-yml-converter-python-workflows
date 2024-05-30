import sys
import json


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


if __name__ == "__main__":
    pathFile1, pathFile2 = parse_args()
    if pathFile1.endswith(".json"):
        data = read_json(pathFile1)
        print(data)
