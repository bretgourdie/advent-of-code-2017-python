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

    def wasCaught(self):
        return self.scannerIndex == 0
    
    def getSeverity(self):
        if self.wasCaught():
            return self.range * self.depth
        else:
            return 0


def splitDepthAndRange(rawDepthRange):
    theSplit = rawDepthRange.split(": ")
    return (theSplit[0], theSplit[1].strip())

rawDepthRanges = []
with open("input.txt", "r") as depthRangeFile:
    rawDepthRanges = depthRangeFile.readlines()

depthToScanner = {}
for rawDepthRange in rawDepthRanges:
    strDepth, strRange = splitDepthAndRange(rawDepthRange)
    depthToScanner[int(strDepth)] = Scanner(int(strDepth), int(strRange))

maxDepth = max([int(depth) for depth in depthToScanner])
totalSeverity = 0
maxDepthRange = range(maxDepth + 1)
for curDepth in maxDepthRange:

    if curDepth in depthToScanner:
        scanner = depthToScanner[curDepth]
        totalSeverity += scanner.getSeverity()

    for depth, scanner in depthToScanner.items():
        scanner.tick()

print("Total severity: {}".format(totalSeverity))
