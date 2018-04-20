def getLargestRegisterValue(valueByRegister):
    return max(v for k, v in valueByRegister.items())

def getMultiplicand(action):
    if action == "inc":
        return 1
    elif action == "dec":
        return -1
    return 0

def conditionSuccessful(registerValue, conditionSign, immediate):
    if conditionSign == ">":
        return registerValue > immediate
    elif conditionSign == "<":
        return registerValue < immediate
    elif conditionSign == ">=":
        return registerValue >= immediate
    elif conditionSign == "<=":
        return registerValue <= immediate
    elif conditionSign == "==":
        return registerValue == immediate
    elif conditionSign == "!=":
        return registerValue != immediate

    print("Weird condition \"{}\"".format(conditionSign))
    return None

instructions = []
with open("input.txt", "r") as instructionFile:
    instructions = instructionFile.readlines()

valueByRegister = {}
maxValues = []

for instruction in instructions:
    splitIn = instruction.split()
    
    targetRegister = splitIn[0]
    action = splitIn[1]
    targetImmediate = int(splitIn[2])
    ifWord = splitIn[3]
    sourceRegister = splitIn[4]
    conditionSign = splitIn[5]
    sourceImmediate = int(splitIn[6])

    multiplicand = getMultiplicand(action)

    if sourceRegister not in valueByRegister:
        valueByRegister[sourceRegister] = 0

    sourceRegisterValue = valueByRegister[sourceRegister]

    if conditionSuccessful(sourceRegisterValue, conditionSign, sourceImmediate):
        targetAddor = targetImmediate * getMultiplicand(action)

        if targetRegister not in valueByRegister:
            valueByRegister[targetRegister] = 0

        valueByRegister[targetRegister] += targetAddor

    maxValues.append(getLargestRegisterValue(valueByRegister))

print("Largest value in any register is {}".format(getLargestRegisterValue(valueByRegister)))
print("Largest value in any register at any point in time is {}".format(max(maxValues)))