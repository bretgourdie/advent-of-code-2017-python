from knothash import KnotHash

def floodFill(coordinate, groupState, groupNumber):
    global coordsToGroup
    global grid

    if coordinate not in coordsToGroup:
        x, y = coordinate
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
            cellState = grid[x][y]

            if cellState == groupState:
                coordsToGroup[coordinate] = groupNumber

                floodFill((x-1, y), groupState, groupNumber) # north
                floodFill((x+1, y), groupState, groupNumber) # south
                floodFill((x, y+1), groupState, groupNumber) # east
                floodFill((x, y-1), groupState, groupNumber) # west

def printGrid(grid):
    with open("gridFile.txt", "w") as gridFile:
        for rowIndex, row in enumerate(grid):
            for colIndex, col in enumerate(row):
                toPrint = "#" if col else "."
                gridFile.write(toPrint)
            gridFile.write("\n")

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
    rawBinaryKnotHash = bin(decimalKnotHash)
    binaryKnotHashNo0 = rawBinaryKnotHash[2:]
    binaryKnotHash = "0" * (dimension - len(binaryKnotHashNo0)) + binaryKnotHashNo0


    gridRow = []
    for digit in str(binaryKnotHash):
        gridRow.append(digit == "1")
        usedSquares += digit == "1" if 1 else 0

    grid.append(gridRow)

print("Number of used squares: {}".format(usedSquares))

printGrid(grid)

coordsToGroup = {}
groupNumber = 0
for rowIndex, row in enumerate(grid):
    for colIndex, col in enumerate(row):
         coordinate = (rowIndex, colIndex)

         if coordinate not in coordsToGroup:
             floodFill(coordinate, col, groupNumber)
             groupNumber += 1

print("Number of groups: {}".format(groupNumber))