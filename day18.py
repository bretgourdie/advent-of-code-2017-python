def getRegisterValueOrNumber(arg):
    strippedArg = arg.strip()
    if len(strippedArg) == 1 and str.isalpha(strippedArg):
        global registerToValue
        return registerToValue[arg]
    else:
        return int(arg)

def insertIfNot(arg):
    global registerToValue

    if arg not in registerToValue:
        registerToValue[arg] = 0

def sound(args):
    global lastPlayedSound
    lastPlayedSound = getRegisterValueOrNumber(args[0])

def set(args):
    global registerToValue

    insertIfNot(args[0])

    registerToValue[args[0]] = getRegisterValueOrNumber(args[1])

def add(args):
    global registerToValue

    insertIfNot(args[0])

    registerToValue[args[0]] += getRegisterValueOrNumber(args[1])

def multiply(args):
    global registerToValue

    insertIfNot(args[0])

    registerToValue[args[0]] *= getRegisterValueOrNumber(args[1])

def mod(args):
    global registerToValue

    insertIfNot(args[0])

    registerToValue[args[0]] %= getRegisterValueOrNumber(args[1])

def recover(args):
    if getRegisterValueOrNumber(args[0]) != 0:
        global lastPlayedSound, firstRecoveredSound

        if firstRecoveredSound is None:
            firstRecoveredSound = lastPlayedSound

def jump(args):
    value = getRegisterValueOrNumber(args[0])

    if value > 0:
        global currentInstructionIndex, wasSuccessfulJump
        currentInstructionIndex += getRegisterValueOrNumber(args[1])
        wasSuccessfulJump = True


dictToMethod = {
    "snd": sound,
    "set": set,
    "add": add,
    "mul": multiply,
    "mod": mod,
    "rcv": recover,
    "jgz": jump
}

def getIncrement(instruction):
    global wasSuccessfulJump
    if not wasSuccessfulJump:
        return 1
    else:
        wasSuccessfulJump = False
        return 0

def interpretInstruction(instruction):
    splitInstruction = instruction.split()

    method = dictToMethod[splitInstruction[0]]

    method(splitInstruction[1:])

    global currentInstructionIndex
    currentInstructionIndex += getIncrement(splitInstruction[0])

with open("input.txt", "r") as instructionFile:
    instructions = instructionFile.readlines()

registerToValue = {}
currentInstructionIndex = 0
lastPlayedSound = None
firstRecoveredSound = None
wasSuccessfulJump = False

while currentInstructionIndex >= 0 and currentInstructionIndex < len(instructions) and firstRecoveredSound is None:
    currentInstruction = instructions[currentInstructionIndex]

    interpretInstruction(currentInstruction)


print("First recovered sound is \"{}\"".format(firstRecoveredSound))