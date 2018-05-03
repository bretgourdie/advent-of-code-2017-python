with open("input.txt", "r") as stepsFile:
    steps = int(stepsFile.readline())

numberOfRuns = 2017
buffer = [0]
currentPosition = 0
run = 1
for run in range(1, numberOfRuns + 1):
    currentPosition = (currentPosition + steps) % len(buffer) + 1
    buffer.insert(currentPosition, run)

nextPosition = (currentPosition + 1) % len(buffer)
valueAfterNumberOfRuns = buffer[nextPosition]

print("Value after {} is {}".format(numberOfRuns, valueAfterNumberOfRuns))

numberOfRuns = 50000000
while run <= steps:
    currentPosition = (currentPosition + steps) % len(buffer) + 1
    buffer.insert(currentPosition, run)
    run += 1



targetNumber = 0
indexOfTargetNumber = buffer.index(targetNumber)
nextPosition = (indexOfTargetNumber + 1) % len(buffer)
valueAfterTargetNumber = buffer[nextPosition]

print("Value after {} is {}".format(targetNumber, valueAfterTargetNumber))
