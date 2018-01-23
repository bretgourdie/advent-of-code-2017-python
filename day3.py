from math import sqrt, floor
from sys import maxsize

class Direction():
    Down  = ( 0,  1)
    Left  = (-1,  0)
    Up    = ( 0, -1)
    Right = ( 1,  0)

def getGridBound(toNum):
    sToNum = sqrt(toNum)
    fsToNum = floor(sToNum)

    # Return odd-powered grid ending (for full grid)
    if fsToNum % 2 == 0:
        return fsToNum + 1
    else:
        return fsToNum + 2

def getNextRowAndColumn(row, column, direction):
    newRow = row + direction[1]
    newColumn = column + direction[0]
    return newRow, newColumn

def getDirectionValue(row, column, direction, grid):
    newRow, newColumn = getNextRowAndColumn(row, column, direction)
    return grid[newRow][newColumn]

def generateGrid(toNum):
    dimension = getGridBound(toNum)
    grid = [[0 for x in range(dimension)] for y in range(dimension)]
    middle = dimension // 2
    currentNumber = 1
    direction = Direction.Right
    row, column = middle, middle
    diameter = 0
    nextDirection = {
        Direction.Right: Direction.Up,
        Direction.Up: Direction.Left,
        Direction.Left: Direction.Down,
        Direction.Down: Direction.Right
    }

    while currentNumber <= dimension ** 2:
        if direction in [Direction.Left, Direction.Right]:
            diameter += 1

        for ii in range(min(diameter, dimension)):
            grid[row][column] = currentNumber
            currentNumber += 1
            row, column = getNextRowAndColumn(row, column, direction)
        direction = nextDirection[direction]

    return grid

def findStart(num, grid):
    for row in range(0, len(grid) - 1):
        for col in range(0, len(grid) - 1):
            if grid[row][col] == num:
                return row, col

    return -1, -1

def getSteps(num):
    grid = generateGrid(num)
    row, column = findStart(num, grid)
    steps = 0
    targetNumber = 1

    while grid[row][column] != targetNumber:
        possibleMoves = {
            Direction.Left: getDirectionValue(row, column, Direction.Left, grid),
            Direction.Right: getDirectionValue(row, column, Direction.Right, grid),
            Direction.Up: getDirectionValue(row, column, Direction.Up, grid),
            Direction.Down: getDirectionValue(row, column, Direction.Down, grid)
        }

        print("Possible Moves:\n{}".format(possibleMoves))

        direction = min(possibleMoves, key=possibleMoves.get)
        print("Selected {}".format(direction))
        row, column = getNextRowAndColumn(row, column, direction)

        steps += 1

    return steps


print(getSteps(1))
print(getSteps(12))
print(getSteps(23))
print(getSteps(1024))
