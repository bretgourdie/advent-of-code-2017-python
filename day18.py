class SoundAndRecover():
    def __init__(self):
        self.lastPlayedFrequency = None
        self.recoveredFrequency = None

    def snd(self, frequency):
        self.lastPlayedFrequency = frequency

    def rcv(self, nonZeroCheck):
        if nonZeroCheck != 0:
            if self.recoveredFrequency == None:
                self.recoveredFrequency = self.lastPlayedFrequency

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
        self.sndAndRcvStrategy.snd(value)
        return True

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
        self.sndAndRcvStrategy.rcv(value)
        return True

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

    def getRecoveredFrequency(self):
        return self.sndAndRcvStrategy.recoveredFrequency

with open("input.txt", "r") as instructionsFile:
    instructions = instructionsFile.readlines()

duet = Duet(instructions, SoundAndRecover())

duet.process()

print("The last recovered frequency is {}".format(duet.getRecoveredFrequency()))
