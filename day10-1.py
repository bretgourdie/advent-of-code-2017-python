
lengths = []
with open("input.txt", "r") as lengthsFile:
    lengths = [int(x) for x in lengthsFile.readline().split(",")]

currentPosition = 0
skipSize = 0

stringLength = 256
string = [x for x in range(stringLength)]

for length in lengths:

    pinchedList = []
    for stringSection in range(length):
        offset = (currentPosition + stringSection) % len(string)
        pinchedList.append(string[offset])

    pinchedList.reverse()
    for stringSection in range(length):
        offset = (currentPosition + stringSection) % len(string)
        string[offset] = pinchedList[stringSection]

    currentPosition += length + skipSize
    skipSize += 1

print("First two numbers multiplied are {}".format(string[0] * string[1]))
