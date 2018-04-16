instructions = []
with open("input.txt", "r") as instructionFile:
    instructions = [int(i) for i in instructionFile.readlines()]

index = 0
outerBound = len(instructions)

steps = 0
while index < outerBound and index >= 0:
    currentInstruction = instructions[index]
    instructions[index] += 1

    index += currentInstruction
    steps += 1

print("It took {} steps to escape the instructions".format(steps))
