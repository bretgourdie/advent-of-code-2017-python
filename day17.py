class Part:
    def __init__(self, runs, target, strategy):
        self.runs = runs
        self.target = target
        self.strategy = strategy

with open("input.txt", "r") as stepsFile:
    stepsAfterRun = int(stepsFile.readline())

def firstPartStrategy(buffer, targetNumber):
    targetNumberIndex = buffer.index(targetNumber)

    return buffer[targetNumberIndex + 1]

def secondPartStrategy(buffer, targetIndex):
    return buffer[targetIndex]

def printAnswer(numberOfRuns, targetIndex, answer):
    print("The number at {} after {} runs is {}".format(targetIndex, numberOfRuns, answer))

def spin(numberOfRuns, maxBufferLength, stepsAfterRun, answerStrategy):
    buffer = []
    currentIndex = 0
    
    for run in range(0, numberOfRuns + 1):
        buffer.insert(currentIndex, run)

        if len(buffer) > maxBufferLength + 1:
            buffer.pop()

        currentIndex = ((currentIndex + stepsAfterRun) % (run + 1)) + 1

    return answerStrategy(buffer, maxBufferLength)

parts = [
    Part(2017, 2017, firstPartStrategy),
    Part(50000000, 1, secondPartStrategy)
]

for part in parts:
    result = spin(part.runs, part.target, stepsAfterRun, part.strategy)
    printAnswer(part.runs, part.target, result)
