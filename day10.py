
lengths = []
with open("input.txt", "r") as lengthsFile:
    lengths = [ord(x) for x in lengthsFile.readline()]
    lengths += [17, 31, 73, 47, 23]

numElements =256 
string = [x for x in range(numElements)]

currentPosition = 0
skipSize = 0
for length in lengths:

    slice = []
    for indexOffset in range(length):
        moddedIndexOffset = (currentPosition + indexOffset) % len(string)
        slice.append(string[moddedIndexOffset])

    for indexOffset in range(length):
        moddedIndexOffset = (currentPosition + indexOffset) % len(string)
        string[moddedIndexOffset] = slice[::-1][indexOffset]

    currentPosition += length + skipSize

    skipSize += 1

print("First two numbers multiplied are {}".format(string[0] * string[1]))
