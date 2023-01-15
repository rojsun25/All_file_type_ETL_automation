# import json
# import xml.etree.ElementTree as ET
# import zipfile
# import csv
# # import parquet

# def open_file(file_path):
#     # Get the file extension
#     file_extension = file_path.split(".")[-1]

#     if file_extension == "json":
#         with open(file_path) as json_file:
#             data = json.load(json_file)
#         print("File is a JSON file, and the data is:")
#         print(data)
#     elif file_extension == "xml":
#         tree = ET.parse(file_path)
#         root = tree.getroot()
#         print("File is a XML file, and the data is:")
#         print(root)
#     elif file_extension == "zip":
#         with zipfile.ZipFile(file_path, 'r') as zip_ref:
#             zip_ref.extractall()
#         print("File is a Zip file, and it's been extracted")
#     elif file_extension == "csv":
#         with open(file_path, mode='r') as csv_file:
#             reader = csv.reader(csv_file)
#             for row in reader:
#                 print(row)
#         print("File is a CSV file, and the data is:")
#     # elif file_extension == "parquet":
#     #     df = pq.read_table(file_path).to_pandas()
#     #     print("File is a parquet file, and the data is:")
#     #     print(df)
#     else:
#         print("Unknown file format")


import json
import xml.etree.ElementTree as ET
import zipfile
import pandas as pd


class FileOpener:
    def __init__(self, file_path):
        self.file_path = file_path

    def open_file(self):
        file_extension = self.file_path.split(".")[-1]
        if file_extension == "json":
            with open(self.file_path) as f:
                data = json.load(f)
            print("File is a JSON file and its data is:", data)
        elif file_extension == "xml":
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            print("File is an XML file and its data is:", root.tag)
        elif file_extension == "zip":
            with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
                zip_ref.extractall()
            print("File is a zip file and its data is:")
        elif file_extension == "csv":
            data = pd.read_csv(self.file_path)
            print("File is a CSV file and its data is:\n", data.head())
        elif file_extension == "parquet":
            data = pd.read_parquet(self.file_path)
            print("File is a parquet file and its data is:\n", data.head())
        else:
            print("Invalid file format")


file_path = "example.csv"
file_opener = FileOpener(file_path)
file_opener.open_file()
