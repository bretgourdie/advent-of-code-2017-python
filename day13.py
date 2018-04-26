class Scanner():
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.scannerIndex = 0
        self.stepDirection = 1
        self.lowerBound = -1
        self.scannerIndex = 0

    def tick(self):
        newIndex = self.scannerIndex + self.stepDirection

        if newIndex == self.lowerBound or newIndex == self.range:
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

delayTicks = 1
while True:
    wasCaught = False
    depthToScanner = createDepthToScanner(rawDepthRanges)
    maxDepth = max([int(depth) for depth in depthToScanner])

    for delayTick in range(delayTicks):
        for depth, scanner in depthToScanner.items():
            scanner.tick()

    for curDepth in range(maxDepth + 1):

        if curDepth in depthToScanner:
            scanner = depthToScanner[curDepth]
            wasCaught = wasCaught or scanner.caughtPacket()

        if wasCaught:
            break

        for depth, scanner in depthToScanner.items():
            scanner.tick()

    if not wasCaught:
        break
    else:
        delayTicks += 1

print("Delay needed: {}".format(delayTicks))
