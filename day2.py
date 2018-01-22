import csv
from enum import Enum

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

def getChecksum(strategy):
    with open("input.txt", "r") as csvfile:
        ss = csv.reader(csvfile, delimiter="\t")
        checksumInputs = []

        for strRow in ss:
            row = list(map(int, strRow))
            checksumInput = getChecksumInput(row, strategy)
            checksumInputs.append(checksumInput)

        return sum(checksumInputs)

print(getChecksum(ChecksumStrategy.MinMaxDiff))
print(getChecksum(ChecksumStrategy.EvenDivide))
