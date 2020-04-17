import io
import os
from os import path

# ======= Configuration =======
# New filenames without special characters, each line is a name of one file
filenames_path = "../resources/names.txt"
# Folder where the original files are located
files_input_path = "../resources/Files/"
# Folder where the rename files will be inserted
files_output_path = "../resources/Files/"
# Prefix of the original files need to change
file_prefix = "teste2-"


def rename():
    filenames = io.open(filenames_path, "r+", encoding="utf8")
    filenames_list = []
    for filename in filenames:
        filename.rstrip()
        filenames_list.append(filename)
    # for entry in entries:
    # #     print(entry)
    if not path.exists(files_output_path):
        os.mkdir(files_output_path)
    entries = os.listdir(files_input_path)
    i = 0
    for entry in entries:
        old_filename = files_input_path + entry
        new_filename = files_output_path + filenames_list[i].rstrip() + ".pdf"
        print("converted: " + old_filename + ", to: " + new_filename)
        os.rename(old_filename, new_filename)
        i += 1


# Add 0 prefix to the filename
def special_cases(file_prefix, n):
    for i in range(1, n + 1):
        old_filename = files_input_path + file_prefix + i.__str__() + ".pdf"
        new_filename = files_input_path + file_prefix + "0" + i.__str__() + ".pdf"
        print("renamed: " + old_filename + ", to: " + new_filename)
        os.rename(old_filename, new_filename)


if __name__ == "__main__":
    special_cases(file_prefix, 9)
    rename()
