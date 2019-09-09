class Part:
    def __init__(self, runs, targetIndex, strategy):
        self.runs = runs
        self.targetIndex = targetIndex
        self.strategy = strategy

with open("input.txt", "r") as stepsFile:
    stepsAfterRun = int(stepsFile.readline())

def firstQuestionAnswerStrategy(buffer, targetNumber):
    targetNumberIndex = buffer.index(targetNumber)

    return buffer[targetNumberIndex + 1]

def secondQuestionAnswerStrategy(buffer, targetIndex):
    return buffer[targetIndex]

def printAnswer(numberOfRuns, targetIndex, answer):
    print("The number at {} after {} runs is {}".format(targetIndex, numberOfRuns, answer))

def spin(numberOfRuns, targetIndex, stepsAfterRun, answerStrategy):
    buffer = []
    currentIndex = 0
    
    for run in range(0, numberOfRuns + 1):
        buffer.insert(currentIndex, run)

        if len(buffer) > targetIndex + 1:
            buffer.pop()

        currentIndex = ((currentIndex + stepsAfterRun) % (run + 1)) + 1

    return answerStrategy(buffer, targetIndex)

parts = [
    Part(2017, 2017, firstQuestionAnswerStrategy),
    Part(50000000, 1, secondQuestionAnswerStrategy)
]

for part in parts:
    result = spin(part.runs, part.targetIndex, stepsAfterRun, part.strategy)
    printAnswer(part.runs, part.targetIndex, result)
