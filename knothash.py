class KnotHash():
    def generateHash(self, input):

        standardLengthSuffixValues = [17, 31, 73, 47, 23]
        lengths = [ord(x) for x in input] + standardLengthSuffixValues

        currentPosition = 0
        skipSize = 0

        stringLength = 256
        string = [x for x in range(stringLength)]

        numberOfRounds = 64

        for round in range(numberOfRounds):

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

        denseHashDecimal = []
        numDenseHashElements = 16

        for denseHashElementIndex in range(numDenseHashElements):
            denseHashElement = 0
            for elementNumber in range(numDenseHashElements):
                elementIndex = elementNumber + denseHashElementIndex * numDenseHashElements
                element = string[elementIndex]
                denseHashElement ^= element

            denseHashDecimal.append(denseHashElement)


        hexRepresentation = []
        for denseHashElement in denseHashDecimal:
            denseHashHex = hex(denseHashElement)
            denseHashHexNoPrefix = denseHashHex[2:]
            paddedDenseHashHexNoPrefix = denseHashHexNoPrefix.zfill(2)
            hexRepresentation.append(paddedDenseHashHexNoPrefix)

        stringHexRepresentation = "".join(hexRepresentation)

        return stringHexRepresentation
