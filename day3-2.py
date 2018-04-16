from math import sqrt, floor
from sys import maxsize
from enum import Enum

class Direction(Enum):
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
    newRow = row + direction.value[1]
    newColumn = column + direction.value[0]
    return newRow, newColumn

def getDirectionValue(row, column, direction, grid):
    newRow, newColumn = getNextRowAndColumn(row, column, direction)
    if newRow < len(grid) and newColumn < len(grid[newRow]):
        return grid[newRow][newColumn]
    else:
        return maxsize

def getNextNumberForPart2(newRow, newColumn, grid, dimension):
    if newRow >= 0 and newColumn >= 0 and newRow < dimension and newColumn < dimension and grid[newRow][newColumn] != None and grid[newRow][newColumn] != 0:
        return grid[newRow][newColumn]
    else:
        return 0

def getNextNumber(currentNumber, row, column, grid, dimension, isPart1):
    if isPart1:
        return currentNumber + 1
    else:
        ul = getNextNumberForPart2(row-1, column-1, grid, dimension)
        u = getNextNumberForPart2(row-1, column, grid, dimension)
        ur = getNextNumberForPart2(row-1, column+1, grid, dimension)

        l = getNextNumberForPart2(row, column-1, grid, dimension)
        r = getNextNumberForPart2(row, column+1, grid, dimension)

        dl = getNextNumberForPart2(row+1, column-1, grid, dimension)
        d = getNextNumberForPart2(row+1, column, grid, dimension)
        dr = getNextNumberForPart2(row+1, column+1, grid, dimension)

        nextNumber = ul + u + ur + l + r + dl + d + dr
        
        return nextNumber


def generateGrid(toNum, isPart1):
    dimension = getGridBound(toNum)
    grid = [[0 for x in range(dimension)] for y in range(dimension)]
    middle = dimension // 2
    currentNumber = 1
    previousNumber = 1
    numberOfCellsPopulated = 0
    direction = Direction.Right
    row, column = middle, middle
    diameter = 0
    hasStatedNextNumber = False
    nextDirection = {
        Direction.Right: Direction.Up,
        Direction.Up: Direction.Left,
        Direction.Left: Direction.Down,
        Direction.Down: Direction.Right
    }

    while numberOfCellsPopulated < dimension ** 2:
        if direction in [Direction.Left, Direction.Right]:
            diameter += 1

        for ii in range(min(diameter, dimension)):
            previousNumber = currentNumber
            if numberOfCellsPopulated > 0:
                currentNumber = getNextNumber(currentNumber, row, column, grid, dimension, isPart1)
            else:
                currentNumber = 1

            if previousNumber <= 289326 and currentNumber > 289326 and not isPart1 and not hasStatedNextNumber:
                print("After {} is {}".format(previousNumber, currentNumber))
                hasStatedNextNumber = True

            grid[row][column] = currentNumber

            row, column = getNextRowAndColumn(row, column, direction)
            numberOfCellsPopulated += 1
        direction = nextDirection[direction]


    return grid

def findStart(num, grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == num:
                return row, col

    return -1, -1

def getSteps(num, isPart1):
    grid = generateGrid(num, isPart1)
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

        direction = min(possibleMoves, key=possibleMoves.get)
        row, column = getNextRowAndColumn(row, column, direction)

        steps += 1

    return steps

tests = [1, 12, 23, 1024, 289326 * 2]
parts = [True, False]
for test in tests:
    for part in parts:
        partDescription = "1" if part else "2"
        print(
            "Number of steps to {} is {} for part {}".format(test, getSteps(test, part), partDescription)
        )

