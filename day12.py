def getSourceAssociationSplit(pipe):
    return pipe.split(" <-> ")

def getSource(pipe):
    return getSourceAssociationSplit(pipe)[0]

def getAssociations(pipe):
    return [x.strip() for x in getSourceAssociationSplit(pipe)[1].split(", ")]

def canAssociate(source, associations, currentPath):
    global processedSources 
    global associationsBySource
    global targetSource

    if targetSource in associations or source == targetSource or source in processedSources:
        for association in associations:
            processedSources[association] = True
        return True

    if source in currentPath:
        return False

    for association in associations:
        canGetToTarget = False
        if association not in processedSources:
            result = canAssociate(association, associationsBySource[association], currentPath + [source])
            canGetToTarget = canGetToTarget or result

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
processedSources = {}

for source, associations in associationsBySource.items():
    if source not in processedSources:
        result = canAssociate(source, associations, [])
        processedSources[source] = result

referencingSources = [source for source, doesReference in processedSources.items() if doesReference]
print("Number of programs in group that contains program ID {} is {}".format(targetSource, len(referencingSources)))
