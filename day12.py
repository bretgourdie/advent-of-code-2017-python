def getSourceAssociationSplit(pipe):
    return pipe.split(" <-> ")

def getSource(pipe):
    return getSourceAssociationSplit(pipe)[0]

def getAssociations(pipe):
    return getSourceAssociationSplit(pipe)[1].split(", ")

def canAssociate(source, associations, associationsBySource, targetSource, originator, firstIteration):
    if targetSource in associations or source == targetSource:
        return True

    if not firstIteration and source == originator:
        return False

    canGetToTarget = False
    for association in associations:
        newAssociations = associationsBySource[association]
        canGetToTarget = canGetToTarget or canAssociate(association, newAssociations, associationsBySource, targetSource, originator, True)

    return canGetToTarget

pipes = []
with open("input.txt", "r") as pipesFile:
    pipes = pipesFile.readlines()

associationsBySource = {}
for pipe in pipes:
    source = getSource(pipe)
    associations = getAssociations(pipe)

    associationsBySource[source] = associations

targetSource = "0"
referencingSources = []

for source, associations in associationsBySource.items():
    if canAssociate(source, associations, associationsBySource, targetSource, source, False):
        referencingSources.append(source)

print("Number of programs in group that contains program ID {} is {}".format(targetSource, len(referencingSources)))
