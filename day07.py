class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def getSideOfArrow(instruction, getLeftSide):
    splitAtArrow = instruction.split(" -> ")

    if getLeftSide:
        return splitAtArrow[0]
    else:
        if len(splitAtArrow) > 1:
            return splitAtArrow[1]
        else:
            return ""

def getLeftSideOfArrow(instruction):
    return getSideOfArrow(instruction, True)

def getRightSideOfArrow(instruction):
    return getSideOfArrow(instruction, False)

def getName(instruction):
    leftSide = getLeftSideOfArrow(instruction)
    spaceSplit = leftSide.split()
    return spaceSplit[0]

def getWeight(instruction):
    leftSide = getLeftSideOfArrow(instruction)
    spaceSplit = leftSide.split()
    scrubbedInt = spaceSplit[1].replace("(", "").replace(")", "")
    return int(scrubbedInt)

def getChildren(instruction):
    rightSide = getRightSideOfArrow(instruction)
    rightSideScrubbed = rightSide.replace(",", "")
    rightSideList = rightSideScrubbed.split()
    if len(rightSideList) > 0 and len(rightSideList[0]) > 0:
        return rightSideList
    else:
        return []

def isInconsistent(frequencyByChildStackWeight):
    return len(frequencyByChildStackWeight) > 1

def getWeightOfStack(node, depth):
    stackWeightByChildNodes = {}
    frequencyByChildStackWeight = {}
    
    for childName in node.children:
        childNode = nodeLookup[childName]
        childStackWeight = getWeightOfStack(childNode, depth+1)
        stackWeightByChildNodes[childNode] = childStackWeight

        if childStackWeight not in frequencyByChildStackWeight:
            frequencyByChildStackWeight[childStackWeight] = 0
        frequencyByChildStackWeight[childStackWeight] += 1

    if isInconsistent(frequencyByChildStackWeight):
        singleWeight = -1
        multiWeight = -1
        for childWeight, freq in frequencyByChildStackWeight.items():
            if freq == 1:
                singleWeight = childWeight
            else:
                multiWeight = childWeight

        for childNode, stackWeight in stackWeightByChildNodes.items():
            if singleWeight == stackWeight:
                print("Inconsistent child {}: weight {} should be {}".format(childNode.name, childNode.weight, childNode.weight - (singleWeight - multiWeight)))

    childrenStackWeight = 0
    for childNode, childWeight in stackWeightByChildNodes.items():
        childrenStackWeight += childWeight

    return childrenStackWeight + node.weight

instructions = []
with open("input.txt", "r") as instructionFile:
    instructions = instructionFile.readlines()

nodeLookup = {}
nodeNames = []
for instruction in instructions:

    children = getChildren(instruction)
    name = getName(instruction)
    weight = getWeight(instruction)

    node = Node(name, weight, children)
    nodeLookup[node.name] = node
    nodeNames.append(node.name)

nodesThatAreRoot = nodeNames[:]

for nodeName in nodeNames:
    node = nodeLookup[nodeName]
    for child in node.children:
        nodesThatAreRoot.remove(child)

rootNodeName = nodesThatAreRoot[0]
print("Root node: \"{}\"".format(rootNodeName))

rootNode = nodeLookup[rootNodeName]
getWeightOfStack(rootNode, 0)
