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
        if register not in self.registers:
            self.registers[register] = 0

    def __getValueFromRegisterOrImmediate(self, value):
        if value in self.registers:
            return registers[value]
        else:
            return value

    def snd(self, value):
        self.sndAndRcvStrategy.snd(value)

    def set(self, register, value):
        self.registers[register] = value

    def add(self, register, value):
        __initRegister(register)
        self.registers[register] += value

    def mul(self, register, value):
        ___initRegister(register)
        self.registers[register] *= value

    def mod(self, register, value):
        __initRegister(register)
        self.registers[register] = registers[register] % value

    def rcv(self, value):
        self.sndAndRcvStrategy.rcv(value)

    def jgz(self, greaterThanZeroCheck, offset):
        if greaterThanZeroCheck > 0:
            self.index += offset

    def process(self):
        while self.index >= 0 and self.index < len(self.instructions):
            instructionLine = self.instructions[index]
            splitInstruction = instructionLine.split()
            instruction = splitInstruction[0]

            function = self.instructionToFunction[instruction]
            function(splitInstruction[1:])

