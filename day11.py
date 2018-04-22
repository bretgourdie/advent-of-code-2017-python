def getMovement(notation):
    if notation == "n":
        return (0, 1, -1)
    elif notation == "nw":
        return (-1, 1, 0)
    elif notation == "ne":
        return (1, 0, -1)
    elif notation == "s":
        return (0, -1, 1)
    elif notation == "sw":
        return (-1, 0, 1)
    elif notation == "se":
        return (1, -1, 0)
    else:
        return (None, None, None)

steps = []
with open("input.txt", "r") as stepsFile:
    steps = [step.strip() for step in stepsFile.readline().split(",")]

x, y, z = (0, 0, 0)

furthestEverGot = 0

for step in steps:
    moveX, moveY, moveZ = getMovement(step)
    x += moveX
    y += moveY
    z += moveZ
    
    currentCoords = [abs(x), abs(y), abs(z)]
    
    if max(currentCoords) > furthestEverGot:
        furthestEverGot = max(currentCoords)

coords = [abs(x), abs(y), abs(z)]

stepsAway = max(coords)
print("Child is {} steps away".format(stepsAway))
print("Furthest child ever got was {} steps away".format(furthestEverGot))
