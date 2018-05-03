def spin(args, programs):
    numToMove = int(args)
    sliceToMove = programs[-numToMove:]
    currentBeginningSlice = programs[0:len(programs) - numToMove]

    programs = sliceToMove + currentBeginningSlice

    return programs

def exchange(args, programs):
    positions = args.split("/")
    posA, posB = int(positions[0]), int(positions[1])

    programs[posA], programs[posB] = programs[posB], programs[posA]

    return programs

def partner(args, programs):
    partners = args.split("/")
    partnerA, partnerB = partners[0], partners[1]

    posA = programs.index(partnerA)
    posB = programs.index(partnerB)

    exchange(str(posA) + "/" + str(posB), programs)

    return programs

def interpretDanceMove(move, programs):
    moveLetter = move[0]
    args = move[1:]
    if moveLetter == "s":
        programs = spin(args, programs)
    elif moveLetter == "x":
        programs = exchange(args, programs)
    elif moveLetter == "p":
        programs = partner(args, programs)
    else:
        print("Unknown move letter {}".format(moveLetter))

    return programs

danceMoves = []
with open("input.txt", "r") as danceMoveFile:
    danceMoves = [x.strip() for x in danceMoveFile.readline().split(",")]

numberOfPrograms = 16
programs = [chr(x) for x in range(ord("a"), ord("a") + numberOfPrograms)]
originalPrograms = programs[:]

numberOfDances = 1000000000
cycles = []
currentDance = 0
for currentDance in range(numberOfDances):
    if programs not in cycles:
        cycles.append(currentDance)
    else:
        break

    for danceMove in danceMoves:
        programs = interpretDanceMove(danceMove, programs)

    if currentDance == 0:
        print("Program order: {}".format("".join(programs)))

cycleStart = cycles.index(programs)
cycleEnd = len(cycles)
cycleLength = cycleEnd - cycleStart

while currentDance + cycleLength < numberOfDances:
    currentDance += cycleLength

for nonCycleCurrentDance in range(currentDance, numberOfDances):
    for danceMove in danceMoves:
        programs = interpretDanceMove(danceMove, programs)

print("Program order: {}".format("".join(programs)))
