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

def getInconsistentWeight(weightByChild):
    if len(weightByChild) == 1:
        return None, None, None

    weightFrequency = {}
    for child in weightByChild:
        weight = weightByChild[child]

        if weight not in weightFrequency:
            weightFrequency[weight] = 0
        weightFrequency[weight] += 1

    if len(weightFrequency) == 1:
        return None, None, None

    singleWeight = -1
    for weight in weightFrequency:
        frequency = weightFrequency[weight]
        if frequency == 1:
            print("SingleWeight: {} (freq: {})".format(weight, frequency))
            singleWeight = weight
            break

    multiWeight = -1
    for weight in weightFrequency:
        frequency = weightFrequency[weight]
        if frequency != 1:
            print("MultiWeight: {} (freq : {})".format(weight, frequency))
            multiWeight = weight
            break

    for child in weightByChild:
        if singleWeight == weightByChild[child]:
            return child, singleWeight, singleWeight - multiWeight

    # Oh well
    return None, None, None

def getWeightOfStack(node, depth):
    stackWeight = 0
    weightByChild = {}
    for child in node.children:
        childStackWeight = getWeightOfStack(nodeLookup[child], depth+1)
        stackWeight += childStackWeight
        weightByChild[child] = childStackWeight

    totalWeight = stackWeight + node.weight

    print(
        "Node {} at depth {} holds {} (stack weight {}; own weight {})".format(
            node.name,
            depth+1,
            totalWeight,
            stackWeight,
            node.weight
        )
    )

    inconsistentChildNode, inconsistentChildNodeWeight, differenceBetweenInconsistentAndConsistent = getInconsistentWeight(weightByChild)

    if inconsistentChildNode is not None:
        actualNode = nodeLookup[inconsistentChildNode]
        print("Inconsistent Child at depth {}: {} (weight: {}, stackweight: {}), InconsistentWeight - ConsistentWeight = {}".format
            (
                depth+1,
                inconsistentChildNode,
                actualNode.weight,
                inconsistentChildNodeWeight,
                differenceBetweenInconsistentAndConsistent
            )
        )
        pass

    return totalWeight

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
