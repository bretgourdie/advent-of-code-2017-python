from knothash import KnotHash

lengths = []
with open("input.txt", "r") as lengthsFile:
    lengths = lengthsFile.readline().strip()

knothash = KnotHash()
print(knothash.generateHash(lengths))
