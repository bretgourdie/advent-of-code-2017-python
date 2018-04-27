from knothash import KnotHash

inputStr = ""
with open("input.txt", "r") as inputFile:
    inputStr = inputFile.readline().strip()

dimension = 128
knothash = KnotHash()
grid = []
usedSquares = 0
for row in range(dimension):
    currentKnotHashInput = inputStr + "-" + str(row)
    
    currentKnotHash = knothash.generateHash(currentKnotHashInput)
    decimalKnotHash = int(currentKnotHash, 16)
    binaryKnotHash = bin(decimalKnotHash)

    gridRow = []
    for digit in str(binaryKnotHash)[2:]:
        gridRow.append(digit == "1")
        usedSquares += digit == "1" if 1 else 0

    grid.append(gridRow)

print("Number of used squares: {}".format(usedSquares))