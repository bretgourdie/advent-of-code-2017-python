class Scanner():
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.scannerIndex = 0
        self.stepDirection = 1
        self.__lowerBound = -1

    def tick(self):
        newIndex = self.scannerIndex + self.stepDirection

        if newIndex == self.__lowerBound or newIndex == self.range:
            self.stepDirection *= -1
            newIndex = self.scannerIndex + self.stepDirection

        self.scannerIndex = newIndex

    def caughtPacket(self):
        return self.scannerIndex == 0
    
    def getSeverity(self):
        if self.caughtPacket():
            return self.range * self.depth
        else:
            return 0

class Rider():
    def __init__(self, delay, maxDepth):
        self.delay = delay
        self.depth = 0
        self.maxDepth = maxDepth
        self.wasCaught = False

    def completeWithoutBeingCaught(self):
        return self.depth > self.maxDepth

    def __repr__(self):
        return "Rider delay: {}, depth: {}, successful: {}".format(self.delay, self.depth, self.completeWithoutBeingCaught())

def splitDepthAndRange(rawDepthRange):
    theSplit = rawDepthRange.split(": ")
    return (theSplit[0], theSplit[1].strip())

def createDepthToScanner(rawDepthRanges):
    depthToScanner = {}
    for rawDepthRange in rawDepthRanges:
        strDepth, strRange = splitDepthAndRange(rawDepthRange)
        depthToScanner[int(strDepth)] = Scanner(int(strDepth), int(strRange))

    return depthToScanner

def getRawFile():
    rawDepthRanges = []
    with open("input.txt", "r") as depthRangeFile:
        rawDepthRanges = depthRangeFile.readlines()

    return rawDepthRanges

def getAllSuccessfulRiders(riders):
    return [rider for rider in riders if rider.completeWithoutBeingCaught()]

rawDepthRanges = getRawFile()
depthToScanner = createDepthToScanner(rawDepthRanges)
maxDepth = max([int(depth) for depth in depthToScanner])
totalSeverity = 0
for curDepth in range(maxDepth + 1):

    if curDepth in depthToScanner:
        scanner = depthToScanner[curDepth]
        totalSeverity += scanner.getSeverity()

    for depth, scanner in depthToScanner.items():
        scanner.tick()

print("Total severity: {}".format(totalSeverity))

delayTicks = 0
depthToScanner = createDepthToScanner(rawDepthRanges)
maxDepth = max([int(depth) for depth in depthToScanner])
riders = []

while len(getAllSuccessfulRiders(riders)) == 0:
    riders.append(Rider(delayTicks, maxDepth))

    for rider in riders:
        if rider.depth in depthToScanner:
            scanner = depthToScanner[rider.depth]
            rider.wasCaught = scanner.caughtPacket()
        rider.depth += 1

    for rider in [rider for rider in riders if rider.wasCaught]:
        riders.remove(rider)

    for depth, scanner in depthToScanner.items():
        scanner.tick()

    delayTicks += 1

for rider in getAllSuccessfulRiders(riders):
    print(rider)
