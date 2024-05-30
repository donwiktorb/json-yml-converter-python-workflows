import json


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
    # Add conditions for other file types
    print(data)
