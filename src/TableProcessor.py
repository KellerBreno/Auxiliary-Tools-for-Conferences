import io

# ======= Configuration =======
# Path to the table with the names of those present in the call
input_path = "../resources/attendance.csv"
# input_path = "../resources/pi1205.csv"
# Path to the table with the names of those present in the call
output_path = "../resources/names.csv"
# Minimum number of occurrences to register the presence
minimum_occurrence = 2


# Function: Generate a set with names from an attendence table
# Parameter: path = path of the table containing the data
# Parameter: minimum_occurrence = value of minimum number of occurrences to register the presence
def proccess(input_path, minimum_occurrence):
    text = io.open(input_path, "r+", encoding="utf8")
    cont = 0
    namedict = dict()
    for line in text:
        # Ignore the first two line of the table format
        if cont >= 2:
            line = line.rstrip()
            names = line.split(",")
            for name in names:
                if len(name) != 0:
                    namedict[name] = namedict.setdefault(name, 0) + 1
        cont += 1
    nameset = set()
    for name in namedict.keys():
        if namedict[name] >= minimum_occurrence:
            nameset.add(name.title())
    return nameset


# Function: Generate a set with names from an attendence table
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
