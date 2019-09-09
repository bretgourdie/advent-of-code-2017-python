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

firstQuestionRuns = 2017
firstQuestionTargetIndex = 2017
firstQuestionResult = spin(firstQuestionRuns, firstQuestionTargetIndex, stepsAfterRun, firstQuestionAnswerStrategy)
printAnswer(firstQuestionRuns, firstQuestionTargetIndex, firstQuestionResult)
