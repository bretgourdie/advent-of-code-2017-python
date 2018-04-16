def getOffsetIncrement(offset, isPart1):
    if isPart1:
        return 1
    else:
        if offset >= 3:
            return -1
        else:
            return 1

def getSteps(isPart1):
    instructions = []
    with open("input.txt", "r") as instructionFile:
        instructions = [int(i) for i in instructionFile.readlines()]

    index = 0
    outerBound = len(instructions)

    steps = 0
    while index < outerBound and index >= 0:
        currentInstruction = instructions[index]
        instructions[index] += getOffsetIncrement(currentInstruction, isPart1)

        index += currentInstruction
        steps += 1

    part = "1" if isPart1 else "2"
    print("It took {} steps to escape the instructions for part {}".format(steps, part))

getSteps(True)
getSteps(False)
