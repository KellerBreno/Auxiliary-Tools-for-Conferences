import io

# ======= Configuration =======
# Path to the table with the names of those present in the call
path = "../resources/attendance.csv"
# Minimum number of occurrences to register the presence
minimum_occurrence = 2


# Function: Generate a set with names from an attendence table
# Parameter: path = path of the table containing the data
# Parameter: minimum_occurrence = value of minimum number of occurrences to register the presence
def proccess(path, minimum_occurrence):
    text = io.open(path, "r+", encoding="utf8")
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
    namelist = set()
    for name in namedict.keys():
        if namedict[name] >= minimum_occurrence:
            namelist.add(name.title())
    return namelist


if __name__ == "__main__":
    names = proccess(path, minimum_occurrence)
    for name in names:
        print(name)
