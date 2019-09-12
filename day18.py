from collections import deque

class SoundAndRecover():
    def __init__(self):
        self.lastPlayedFrequency = None
        self.recoveredFrequency = None

    def snd(self, frequency):
        self.lastPlayedFrequency = frequency
        return True

    def rcv(self, nonZeroCheck):
        if nonZeroCheck != 0:
            if self.recoveredFrequency == None:
                self.recoveredFrequency = self.lastPlayedFrequency
        return True

    def shouldEarlyTerminate(self):
        return self.recoveredFrequency != None

class SendAndReceive():
    def __init__(self):
        self.sendingBuffer = deque()
        self.otherSendAndReceive = None
        self.isWaiting = False

    def SetOtherSendAndReceive(otherSendAndReceive):
        self.otherSendAndReceive = otherSendAndReceive

    def snd(self, value):
        self.sendingBuffer.append(value)
        return True

    def rcv(self, register):
        otherSendingBuffer = self.otherSendAndReceive.sendingBuffer
        if len(otherSendingBuffer) > 0:
            value = otherSendingBuffer.popleft()
            #registers[register] = value
            self.isWaiting = False
        else:
            self.isWaiting = True

        return self.isWaiting

    def shouldEarlyTerminate(self):
        pass

class Duet:
    def __init__(self, instructions, sndAndRcvStrategy):
        self.registers = {}
        self.sndAndRcvStrategy = sndAndRcvStrategy
        self.instructions = instructions
        self.index = 0

        self.instructionToFunction = {
            "snd": self.snd,
            "set": self.set,
            "add": self.add,
            "mul": self.mul,
            "mod": self.mod,
            "rcv": self.rcv,
            "jgz": self.jgz
        }

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
        return self.sndAndRcvStrategy.rcv(value)

    def jgz(self, valueOrRegister, offsetValueOrRegister):
        value = self.__getValue(valueOrRegister)
        offset = self.__getValue(offsetValueOrRegister)
        if value > 0:
            self.index += offset
            return False
        else:
            return True

    def process(self):
        while self.index >= 0 and self.index < len(self.instructions):
            instructionLine = self.instructions[self.index]
            splitInstruction = instructionLine.split()
            instruction = splitInstruction[0]

            function = self.instructionToFunction[instruction]
            shouldIncrement = function(*splitInstruction[1:])

            if shouldIncrement:
                self.index += 1

            if self.sndAndRcvStrategy.shouldEarlyTerminate():
                break

    def getRecoveredFrequency(self):
        return self.sndAndRcvStrategy.recoveredFrequency

with open("input.txt", "r") as instructionsFile:
    instructions = instructionsFile.read().splitlines()

duet = Duet(instructions, SoundAndRecover())

duet.process()

print("The last recovered frequency is {}".format(duet.getRecoveredFrequency()))
