import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


import xmltodict
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


def write_xml(file_path, data):
    with open(file_path, "w") as file:
        xml_data = xmltodict.unparse(data, pretty=True)
        file.write(xml_data)


class ConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Data Converter")
        self.setGeometry(100, 100, 600, 400)

        self.input_label = QtWidgets.QLabel(self)
        self.input_label.setText("Input File:")
        self.input_label.move(50, 50)

        self.input_text = QtWidgets.QLineEdit(self)
        self.input_text.setGeometry(150, 50, 400, 30)

        self.output_label = QtWidgets.QLabel(self)
        self.output_label.setText("Output File:")
        self.output_label.move(50, 100)

        self.output_text = QtWidgets.QLineEdit(self)
        self.output_text.setGeometry(150, 100, 400, 30)

        self.convert_button = QtWidgets.QPushButton(self)
        self.convert_button.setText("Convert")
        self.convert_button.setGeometry(250, 150, 100, 30)
        self.convert_button.clicked.connect(self.convert)

    def convert(self):
        input_file = self.input_text.text()
        output_file = self.output_text.text()
        self.thread = threading.Thread(
            target=self.perform_conversion, args=(input_file, output_file)
        )
        self.thread.start()

    def perform_conversion(self, input_file, output_file):
        data = None

        if input_file.endswith(".json"):
            data = read_json(input_file)
        elif input_file.endswith(".yml") or input_file.endswith(".yaml"):
            data = read_yaml(input_file)
        elif input_file.endswith(".xml"):
            data = read_xml(input_file)

        if output_file.endswith(".json"):
            write_json(output_file, data)
        elif output_file.endswith(".yml") or output_file.endswith(".yaml"):
            write_yaml(output_file, data)
        elif output_file.endswith(".xml"):
            write_xml(output_file, data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConverterApp()
    converter.show()
    sys.exit(app.exec_())
