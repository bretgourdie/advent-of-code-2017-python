def getMemoryBankWithMostBlocks(memoryBank):
    maxBlocks = -1
    maxBlocksIndex = 0
    for index in range(0, len(memoryBank)):
        currentBlocks = memoryBank[index]

        if currentBlocks > maxBlocks:
            maxBlocksIndex = index
            maxBlocks = currentBlocks

    return maxBlocksIndex

def getNextMemoryBankIndex(memoryBank, index):
    return (index + 1) % len(memoryBank)

def redistributeBlocks(memoryBank):
    indexToRedistribute = getMemoryBankWithMostBlocks(memoryBank)
    blocksToRedistribute = memoryBank[indexToRedistribute]
    memoryBank[indexToRedistribute] = 0

    index = getNextMemoryBankIndex(memoryBank, indexToRedistribute)
    while blocksToRedistribute > 0:
        memoryBank[index] += 1
        blocksToRedistribute -= 1
        index = getNextMemoryBankIndex(memoryBank, index)

memoryBank = []
with open("input.txt", "r") as memoryBankFile:
    rawLine = memoryBankFile.readline()
    memoryBank = [int(i) for i in rawLine.split()]

numberOfRedistributions = 0
memoryBankConfigurations = []

while memoryBank not in memoryBankConfigurations:
    memoryBankConfigurations.append(memoryBank[:])
    
    redistributeBlocks(memoryBank)
    numberOfRedistributions += 1

print("Took {} redistributions to find a loop".format(numberOfRedistributions))

sizeOfLoop = 0
loopBeginning = memoryBank[:]
print("Loop beginning: {}".format(loopBeginning))
while True:
    redistributeBlocks(memoryBank)
    sizeOfLoop += 1

    if memoryBank == loopBeginning:
        print("Loop detected; memoryBank: {}".format(memoryBank))
        break


print("Size of loop is {}".format(sizeOfLoop))
