beginGarbageChar = "<"
endGarbageChar = ">"
beginGroupChar = "{"
endGroupChar = "}"
negateChar = "!"

totalPoints = 0
garbageCount = 0

class State:
    def __init__(self, previousState):
        self.previousState = previousState

    def getPreviousState(self):
        return self.previousState

    def __repr__(self):
        return self.__class__.__name__

    def handleChar(self, char, depth=0):
        global totalPoints

        if char == beginGarbageChar:
            return InGarbage(self)
        elif char == endGarbageChar:
            return self.getPreviousState()
        elif char == beginGroupChar:
            return InGroup(self, depth+1)
        elif char == endGroupChar:
            totalPoints += self.depth
            return self.getPreviousState()
        elif char == negateChar:
            return SkipNextChar(self)
        else:
            return self

class Initial(State):
    def handleChar(self, char):
        return super().handleChar(char)

class InGroup(State):
    def __init__(self, previousState, depth):
        self.depth = depth
        super().__init__(previousState)

    def handleChar(self, char):
        return super().handleChar(char, self.depth)

    def __repr__(self):
        return self.__class__.__name__ + " (" + str(self.depth) + ")"

class InGarbage(State):
    def handleChar(self, char):
        global garbageCount

        if char == endGarbageChar:
            return self.getPreviousState()
        elif char == negateChar:
            return SkipNextChar(self)
        else:
            garbageCount += 1
            return self

class SkipNextChar(State):
    def handleChar(self, char):
        return self.getPreviousState()

stream = ""
with open("input.txt", "r") as streamFile:
    stream = streamFile.readline()

currentState = Initial(None)
for char in stream:
    currentState = currentState.handleChar(char)

print("CurrentState: {}; totalPoints: {}; garbageCount: {}".format(
    currentState, totalPoints, garbageCount)
)
