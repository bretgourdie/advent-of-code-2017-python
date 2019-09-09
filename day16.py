def sPrograms(programs):
    return "".join(programs)

class Cycler:
    def __init__(self):
        self.fastLookup = set()
        self.indexer = []
        self.cycleDetected = False
        self.cycleLength = -1
        self.cycleStart = -1
        self.cycleEnd = -1

    def add(self, programs):
        sp = sPrograms(programs)

        self.indexer.append(sp)

        self.cycleDetected = sp in self.fastLookup

        if sp not in self.fastLookup:
            self.fastLookup.add(sp)

        else:
            self.cycleStart = self.indexer.index(sp)
            self.cycleEnd = self.indexer.index(sp, self.cycleStart + 1)
            self.cycleLength = self.cycleEnd - self.cycleStart

def spin(programs, args):
    sliceToSpin = int(args)
    length = len(programs)
    pivot = length - sliceToSpin
    spinningToFront = programs[-sliceToSpin:]
    remainder = programs[:pivot]
    return spinningToFront + remainder

def swap(programs, posA, posB):
    swappingPrograms = programs[:]

    swappingPrograms[posA], swappingPrograms[posB] = swappingPrograms[posB], swappingPrograms[posA]

    return swappingPrograms

def exchange(programs, args):
    sPosA, sPosB = args.split("/")

    posA, posB = int(sPosA), int(sPosB)

    return swap(programs, posA, posB)

def partner(programs, args):
    progA, progB = args.split("/")

    posA = programs.index(progA)
    posB = programs.index(progB)

    return swap(programs, posA, posB)

def interpretDanceMove(programs, danceMove):
    movement = danceMove[0]
    args = danceMove[1:]

    if movement == "s":
        return spin(programs, args)
    elif movement == "x":
        return exchange(programs, args)
    elif movement == "p":
        return partner(programs, args)

def performFullDance(programs, danceMoves):
    for danceMove in danceMoves:
        programs = interpretDanceMove(programs, danceMove)

    return programs

danceMoves = []
with open("input.txt", "r") as danceMoveFile:
    danceMoves = [x.strip() for x in danceMoveFile.readline().split(",")]

numberOfPrograms = 16
programs = [chr(x) for x in range(ord("a"), ord("a") + numberOfPrograms)]
cycler = Cycler()
numberOfDanceThroughs = 1000000000000

for danceThrough in range(numberOfDanceThroughs):

    cycler.add(programs)

    if (cycler.cycleDetected):
        break

    programs = performFullDance(programs, danceMoves)

    if danceThrough == 0:
        print("Programs after first dance: {}".format(sPrograms(programs)))

remainingDances = (numberOfDanceThroughs - cycler.cycleStart - cycler.cycleLength) % cycler.cycleLength

for danceThrough in range(remainingDances):
    programs = performFullDance(programs, danceMoves)

print("Programs after {} dances: {}".format(numberOfDanceThroughs, sPrograms(programs)))
