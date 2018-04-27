class KnotHash():
    def generateHash(self, input):
        lengths = [ord(x) for x in input]
        lengths += [17, 31, 73, 47, 23]

        numElements = 256 
        numRounds = 64
        string = [x for x in range(numElements)]

        currentPosition = 0
        skipSize = 0

        for round in range(numRounds):
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

        denseHash = []
        numNumbersInDenseHash = 16

        for hashElementNumber in range(numNumbersInDenseHash):
            hashElement = 0
            for blockElement in range(numNumbersInDenseHash):
                hashElement ^= string[hashElementNumber * 16 + blockElement]
            denseHash.append(hashElement)

        hexString = ""
        for denseHashElement in denseHash:
            hexString += hex(denseHashElement)[2:]

        return hexString.zfill(32)
