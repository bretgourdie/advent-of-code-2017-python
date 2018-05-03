with open("input.txt", "r") as stepsFile:
    steps = int(stepsFile.readline())

numberOfRuns = 2017
buffer = [0]
currentPosition = 0
for run in range(1, numberOfRuns + 1):
    currentPosition = (currentPosition + steps) % len(buffer) + 1
    buffer.insert(currentPosition, run)

nextPosition = (currentPosition + 1) % len(buffer)
valueAfterNumberOfRuns = buffer[nextPosition]

print("Value after {} is {}".format(numberOfRuns, valueAfterNumberOfRuns))