class SoundAndRecover():
    def __init__(self):
        self.lastPlayedFrequency = None
        self.recoveredFrequency = None

    def snd(self, frequency):
        self.lastPlayedFrequency = frequency

    def rcv(self, nonZeroCheck):
        if nonZeroCheck != 0:
            if self.recoveredFrequency != None:
                self.recoveredFrequency = self.lastPlayedFrequency

class Duet:
    def __init__(self, instructions, sndAndRcvStrategy):
        self.registers = {}
        self.sndAndRcvStrategy = sndAndRcvStrategy
        self.instructions = instructions
        self.index = 0
        self.shouldIncrement = True

        self.instructionToFunction = {
            "snd": self.snd,
            "set": self.set,
            "add": self.add,
            "mul": self.mul,
            "mod": self.mod,
            "rcv": self.rcv,
            "jgz": self.jgz
        }

    def __handleShouldIncrement(self, cameFromJgz):
        self.shouldIncrement = not cameFromJgz

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

    def set(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] = value

    def add(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] += value

    def mul(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] *= value

    def mod(self, register, valueOrRegister):
        self.__initRegister(register)
        value = self.__getValue(valueOrRegister)
        self.registers[register] = registers[register] % value

    def rcv(self, valueOrRegister):
        value = self.__getValue(valueOrRegister)
        self.sndAndRcvStrategy.rcv(value)

    def jgz(self, valueOrRegister, offsetValueOrRegister):
        value = self.__getValue(valueOrRegister)
        offset = self.__getValue(valueOrRegister)
        if value > 0:
            self.index += offset

    def process(self):
        while self.index >= 0 and self.index < len(self.instructions):
            instructionLine = self.instructions[self.index]
            splitInstruction = instructionLine.split()
            instruction = splitInstruction[0]

            function = self.instructionToFunction[instruction]
            function(*splitInstruction[1:])

            if self.__handleShouldIncrement:
                self.index += 1

    def getRecoveredFrequency(self):
        return self.sndAndRcvStrategy.recoveredFrequency

with open("input.txt", "r") as instructionsFile:
    instructions = instructionsFile.readlines()

duet = Duet(instructions, SoundAndRecover())

duet.process()

print("The last recovered frequency is {}".format(duet.getRecoveredFrequency()))
