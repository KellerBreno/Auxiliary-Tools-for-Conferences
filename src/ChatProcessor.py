import io
import re

DEBUG = False

# ======= Configuration =======
# Path to the chat with the names of those present in the call
input_path = "../resources/sample_chat.sbv" if DEBUG else "../resources/pi1205.sbv"
# Path to the table with the names of those present in the call
output_path = "../resources/names.csv" if DEBUG else "../resources/names_sbv.csv"
# Minimum number of occurrences to register the presence
minimum_occurrence = 1 if DEBUG else 1


# Function: Generate a set with names from an logged chat table
# Parameter: path = path of the chat log file
# Parameter: minimum_occurrence = value of minimum number of occurrences to register the presence
def proccess(input_path, minimum_occurrence):
    text = io.open(input_path, "r+", encoding="utf8")
    namedict = dict()
    for line in text:
        found = re.search("[A-zÀ-ÿ\.' ]+:", line)
        if found is not None:
            name = found.group(0).replace(":", "")
            namedict[name] = namedict.setdefault(name, 0) + 1
    nameset = set()
    for name in namedict.keys():
        if namedict[name] >= minimum_occurrence:
            nameset.add(name.title())
    return nameset


# Function: Generate a set with names from an logged chat
# Parameter: output_path = path of csv with the names will be saved
# Parameter: namelist = set with the names to be write
def export(output_path, nameset):
    output_file = open(output_path, "w+", encoding="utf8")
    output_file.write("Nomes\n")
    namelist = list()
    for name in nameset:
        namelist.append(name)
    namelist.sort()
    for name in namelist:
        output_file.write(name)
        output_file.write("\n")


if __name__ == "__main__":
    names = proccess(input_path, minimum_occurrence)
    export(output_path, names)
