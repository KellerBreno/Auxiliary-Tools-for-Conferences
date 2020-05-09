import io

# ======= Configuration =======
# Path to the table with the names of those present in the call
path = "../resources/attendance.csv"


def proccess(path):
    text = io.open(path, "r+", encoding="utf8")
    cont = 0
    nameslist = set()
    for line in text:
        if cont >= 2:
            line = line.rstrip()
            names = line.split(",")
            for name in names:
                if len(name) != 0:
                    nameslist.add(name)
        cont += 1
    return nameslist


if __name__ == "__main__":
    names = proccess(path)
    for name in names:
        print(name)
