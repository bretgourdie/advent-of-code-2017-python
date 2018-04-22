import csv
from enum import Enum
from sys import argv

class ChecksumStrategy(Enum):
    MinMaxDiff = 1,
    EvenDivide = 2

def getEvenDivide(row):
    for num1 in row:
        for num2 in row:
            if num1 != num2:
                iMax = max(num1, num2)
                iMin = min(num1, num2)
                if iMax // iMin == iMax / iMin:
                    return iMax // iMin

def getChecksumInput(row, strategy):
    if strategy == ChecksumStrategy.MinMaxDiff:
        return max(row) - min(row)
    elif strategy == ChecksumStrategy.EvenDivide:
        return getEvenDivide(row)

def getChecksum(filename, strategy):
    with open(filename, "r") as csvfile:
        ss = csv.reader(csvfile, delimiter="\t")
        checksumInputs = []

        for strRow in ss:
            row = list(map(int, strRow))
            checksumInput = getChecksumInput(row, strategy)
            checksumInputs.append(checksumInput)

        return sum(checksumInputs)

if len(argv) > 1:
    print(getChecksum(argv[1], ChecksumStrategy.MinMaxDiff))
    print(getChecksum(argv[1], ChecksumStrategy.EvenDivide))
else:
    print("Input filename is required.")
