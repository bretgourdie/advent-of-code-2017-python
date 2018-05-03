def sound(args):
    pass

def set(args):
    global registerToValue

    registerToValue[args[0]] = int(args[1])

def add(args):
    global registerToValue

    registerToValue[args[0]] += int(args[1])

def multiply(args):
    global registerToValue

def mod(args):
    pass

def recover(args):
    pass

def jump(args):
    pass

dictToMethod = {
    "snd": sound,
    "set": set,
    "add": add,
    "mult": multiply,
    "mod": mod,
    "rcv": recover,
    "jgz": jump
}

def interpretInstruction(instruction):
    splitInstruction = instruction.split()

    method = dictToMethod[splitInstruction[0]]

    method(splitInstruction[1:])

with open("input.txt", "r") as instructionFile:
    instructions = instructionFile.readlines()

registerToValue = {}
currentInstructionIndex = 0

while currentInstructionIndex > 0 and currentInstructionIndex < len(instructions):
    currentInstruction = instructions[currentInstructionIndex]

    interpretCommand(currentInstruction)