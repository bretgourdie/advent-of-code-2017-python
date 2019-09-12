from collections import deque

class SoundAndRecover():
    def __init__(self):
        self.lastPlayedFrequency = None
        self.recoveredFrequency = None

    def snd(self, frequency):
        self.lastPlayedFrequency = frequency
        return True

    def rcv(self, valueOrRegister, nonZeroCheck):
        if nonZeroCheck != 0:
            if self.recoveredFrequency == None:
                self.recoveredFrequency = self.lastPlayedFrequency
        return True

    def shouldEarlyTerminate(self):
        return self.recoveredFrequency != None

class SendAndReceive():
    bufferByProgram = {}

    def __init__(self, programId):
        self.otherSendAndReceive = None
        self.isWaiting = False
        self.programId = programId
        self.numberOfSends = 0

        SendAndReceive.bufferByProgram[programId] = deque()

    def snd(self, value):
        SendAndReceive.bufferByProgram[self.programId].append(value)
        self.numberOfSends += 1
        return True

    def rcv(self, valueOrRegister, value):
        otherSendingBufferIndex = (self.programId + 1) % len(SendAndReceive.bufferByProgram)
        otherSendingBuffer = SendAndReceive.bufferByProgram[otherSendingBufferIndex]
        if len(otherSendingBuffer) > 0:
            value = otherSendingBuffer.popleft()
            Duet.registersByProgram[self.programId][valueOrRegister] = value
            self.isWaiting = False
        else:
            self.isWaiting = True

        return not self.isWaiting

    def shouldEarlyTerminate(self):
        return self.isWaiting

class Duet:
    registersByProgram = {}

    def __init__(self, instructions, sndAndRcvStrategy, programId = None):
        self.registers = {}
        self.sndAndRcvStrategy = sndAndRcvStrategy
        self.instructions = instructions
        self.index = 0
        self.receiveBuffer = None
        self.programId = programId

        Duet.registersByProgram[programId] = self.registers

        if programId is not None:
            self.registers["p"] = programId

        self.instructionToFunction = {
            "snd": self.snd,
            "set": self.set,
            "add": self.add,
            "mul": self.mul,
            "mod": self.mod,
            "rcv": self.rcv,
            "jgz": self.jgz
        }

    def setReceiveBuffer(self, duet):
        self.receiveBuffer = duet.sndAndRcvStrategy.sendingBuffer

    def __initRegister(self, register):
        if not register.isalpha():
            return
        
        if register not in self.registers:
            self.registers[register] = 0

    def __getValueFromRegisterOrImmediate(self, value):
        if value in self.registers:
            return self.registers[value]
        else:
            return int(value)

    def __getValue(self, valueOrRegister):
        self.__initRegister(valueOrRegister)
        return self.__getValueFromRegisterOrImmediate(valueOrRegister)

    def snd(self, valueOrRegister):
        value = self.__getValue(valueOrRegister)
        return self.sndAndRcvStrategy.snd(value)

    def set(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] = value
        return True

    def add(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] += value
        return True

    def mul(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] *= value
        return True

    def mod(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] %= value
        return True

    def rcv(self, valueOrRegister):
        value = self.__getValue(valueOrRegister)
        return self.sndAndRcvStrategy.rcv(valueOrRegister, value)

    def jgz(self, valueOrRegister, offsetValueOrRegister):
        value = self.__getValue(valueOrRegister)
        offset = self.__getValue(offsetValueOrRegister)
        if value > 0:
            self.index += offset
            return False
        else:
            return True

    def shouldContinueProcessing(self):
        return self.index >= 0 and self.index < len(self.instructions) and not self.sndAndRcvStrategy.shouldEarlyTerminate()

    def process(self):
        instructionLine = self.instructions[self.index]
        splitInstruction = instructionLine.split()
        instruction = splitInstruction[0]

        function = self.instructionToFunction[instruction]
        shouldIncrement = function(*splitInstruction[1:])

        if shouldIncrement:
            self.index += 1

    def getRecoveredFrequency(self):
        return self.sndAndRcvStrategy.recoveredFrequency

with open("input.txt", "r") as instructionsFile:
    instructions = instructionsFile.read().splitlines()

duet = Duet(instructions, SoundAndRecover())

while duet.shouldContinueProcessing():
    duet.process()

print("The last recovered frequency is {}".format(duet.getRecoveredFrequency()))

duets = [
    Duet(instructions, SendAndReceive(0), 0),
    Duet(instructions, SendAndReceive(1), 1)
]

while any(duet.shouldContinueProcessing() for duet in duets):
    for duet in duets:
        duet.process()

targetProgramId = 1
numberOfSends = duets[targetProgramId].sndAndRcvStrategy.numberOfSends
print("The number of sends program {} sent was {}".format(targetProgramId, numberOfSends))
