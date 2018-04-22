def getMovement(notation):
    if notation == "n":
        return (0, -1)
    elif notation == "nw":
        return (-1, 0)
    elif notation == "ne":
        return (1, -1)
    elif notation == "s":
        return (0, 1)
    elif notation == "sw":
        return (-1, 1)
    elif notation == "se":
        return (1, 0)
    else:
        return (None, None)

steps = []
with open("input.txt", "r") as stepsFile:
    steps = [step.strip() for step in stepsFile.readline().split(",")]

q, r = (0, 0)

for step in steps:
    newQ, newR = getMovement(step)
    q += newQ
    r += newR

stepsAway = None
print("Child is {} steps away".format(stepsAway))