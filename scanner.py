#!/bin/python
import os
import sys
import csv
import os.path
import shutil


#
# Scan a directory for files and output a csv where
# each row contains the information about one file.
#


# Scan un dossier et construit un liste contenant toutes
# les informations (size, path, etc) des fichiers (recursif).
# Les information sont stocker dans des dict
# input: dossier
# output: list de dict (de fichier)
def scanner(path):
    header = ["Name", "Path", "Size", "Executable", "Extension"]
    data_files = []
    root = os.path.join(path)
    for directory, subdir_list, file_list in os.walk(root):
        print('Directory:', directory)
        for name in subdir_list:
            print('Subdirectory:', name)
        for name in file_list:
            print('File:', name)
            file_path = os.path.join(directory, name)
            data = {
                'Name': name,
                'Path': file_path,
                'Size': os.path.getsize(file_path) / 1024,
                'Executable': shutil.which(file_path),
                'Extension': name.split(".")[-1]
            }
            data_files.append(data)

    data_files = sorted(data_file, key=lambda x:x["Size"], reverse=True)
    return data_files, header


# Enregistre une list de dictionnaire au format csv
def write_csv(data_list, header):
    csv_file = "document.csv"
    try:
        with open(csv_file, 'w') as f:
            if os.name == "nt":
                delimiter = ";"
            else:
                delimiter = ","
            writer = csv.DictWriter(f, fieldnames=header, delimiter=delimiter)
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)
    except IOError:
        print("I/O error")


if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    path = "."

data_files, header = scanner(path)
write_csv(data_files, header)

# ./scanner.py [PATH]
