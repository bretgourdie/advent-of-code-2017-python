from enum import Enum

class SndAndRcv(Enum):
    SoundAndRecover = 1
    SendAndReceive = 2

class Duet:
    def __init__(self, programId, sndAndRcv, instructions):
        self.registerToValue = {}
        self.currentInstructionIndex = 0
        self.lastPlayedSound = None
        self.firstRecoveredSound = None
        self.wasSuccessfulJump = False
        self.instructions = instructions
        self.programId = programId

        self.dictToMethod = {
            "set": Duet.setValue,
            "add": Duet.add,
            "mul": Duet.multiply,
            "mod": Duet.mod,
            "jgz": Duet.jump
        }

        if sndAndRcv == SndAndRcv.SoundAndRecover:
            self.dictToMethod["snd"] = Duet.sound
            self.dictToMethod["rcv"] = Duet.recover
        elif sndAndRcv == SndAndRcv.SendAndReceive:
            self.dictToMethod["snd"] = Duet.send
            self.dictToMethod["rcv"] = Duet.receive

    def getRegisterValueOrNumber(self, arg):
        strippedArg = arg.strip()
        if len(strippedArg) == 1 and str.isalpha(strippedArg):
            return self.registerToValue[arg]
        else:
            return int(arg)

    def insertIfNot(self, arg):
        if arg not in self.registerToValue:
            self.registerToValue[arg] = 0

    def sound(self, args):
        self.lastPlayedSound = self.getRegisterValueOrNumber(args[0])

    def send(self, args):
        pass

    def setValue(self, args):
        self.insertIfNot(args[0])

        self.registerToValue[args[0]] = self.getRegisterValueOrNumber(args[1])

    def add(self, args):
        self.insertIfNot(args[0])

        self.registerToValue[args[0]] += self.getRegisterValueOrNumber(args[1])

    def multiply(self, args):
        self.insertIfNot(args[0])

        self.registerToValue[args[0]] *= self.getRegisterValueOrNumber(args[1])

    def mod(self, args):
        self.insertIfNot(args[0])

        self.registerToValue[args[0]] %= self.getRegisterValueOrNumber(args[1])

    def recover(self, args):
        if self.getRegisterValueOrNumber(args[0]) != 0 and self.firstRecoveredSound is None:
            self.firstRecoveredSound = self.lastPlayedSound

    def receive(self, args):
        pass

    def jump(self, args):
        value = self.getRegisterValueOrNumber(args[0])

        if value > 0:
            self.currentInstructionIndex += self.getRegisterValueOrNumber(args[1])
            self.wasSuccessfulJump = True



    def getIncrement(self, instruction):
        if self.wasSuccessfulJump:
            self.wasSuccessfulJump = False
            return 0
        else:
            return 1

    def interpretInstruction(self, instruction):
        splitInstruction = instruction.split()

        method = self.dictToMethod[splitInstruction[0]]

        method(self, splitInstruction[1:])

        self.currentInstructionIndex += self.getIncrement(splitInstruction[0])

    def shouldContinue(self):
        withinLowerBounds = self.currentInstructionIndex >= 0
        withinUpperBounds = self.currentInstructionIndex < len(self.instructions)
        needFirstSound = self.firstRecoveredSound is None
        return (
            withinLowerBounds
            and withinUpperBounds
            and needFirstSound
        )

    def update(self):

        currentInstruction = self.instructions[self.currentInstructionIndex]

        self.interpretInstruction(currentInstruction)


with open("input.txt", "r") as instructionFile:
    instructions = instructionFile.readlines()

soundAndRecoverDuet = Duet(0, SndAndRcv.SoundAndRecover, instructions)

while soundAndRecoverDuet.shouldContinue():
    soundAndRecoverDuet.update()

print("First recovered sound is \"{}\"".format(soundAndRecoverDuet.firstRecoveredSound))

duets = []
numDuets = 2
for i in range(numDuets):
    duets.append(Duet(i, SndAndRcv.SendAndReceive, instructions))

while True:
    for index, duet in enumerate(duets):
        otherDuet = duets[(index + 1) % 2]

    break

