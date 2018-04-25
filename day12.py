def getSourceAssociationSplit(pipe):
    return pipe.split(" <-> ")

def getSource(pipe):
    return getSourceAssociationSplit(pipe)[0]

def getAssociations(pipe):
    return [x.strip() for x in getSourceAssociationSplit(pipe)[1].split(", ")]

def getAllContacts(source, associations, path):
    global sourceToContacts
    global associationsBySource

    if source in path:
        return []

    nonDuplicatedAssociations = [association for association in associations if association != source]

    contacts = [source] + nonDuplicatedAssociations

    for association in nonDuplicatedAssociations:
        subContacts = getAllContacts(association, associationsBySource[association], path + [source])

        for subContact in subContacts:
            if subContact not in contacts:
                contacts.append(subContact)

    return contacts

pipes = []
with open("input.txt", "r") as pipesFile:
    pipes = pipesFile.readlines()

associationsBySource = {}
for pipe in pipes:
    source = getSource(pipe)
    associations = getAssociations(pipe)

    associationsBySource[source] = associations

targetSource = "0"
sourceToContacts = {}

for source, associations in associationsBySource.items():
    sourceToContacts[source] = getAllContacts(source, associations, path=[])

groupToCount = {}
for source, contacts in sourceToContacts.items():
    sortedTupleContacts = tuple(sorted(contacts))

    if sortedTupleContacts not in groupToCount:
        groupToCount[sortedTupleContacts] = 0

    groupToCount[sortedTupleContacts] += 1

for group, count in groupToCount.items():
    if targetSource in group:
        print("Number of programs that contain program ID {} is {}".format(targetSource, count))
        break

print("Number of groups: {}".format(len(groupToCount)))
