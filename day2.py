import csv

def getChecksum():
    with open("input.txt", "r") as csvfile:
        ss = csv.reader(csvfile, delimiter="\t")
        diffs = []

        for strRow in ss:
            row = list(map(int, strRow))
            diff = max(row) - min(row)
            diffs.append(diff)

        return sum(diffs)

print(getChecksum())
