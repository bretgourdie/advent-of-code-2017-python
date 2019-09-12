from enum import Enum

class Direction(Enum):
    Up = (0, -1)
    Down = (0, 1)
    Left = (-1, 0)
    Right = (1, 0)

class Packet():
    Change = ["+"]
    Stop = [" "]

    DirectionToOpposite = {
        Direction.Up: Direction.Down,
        Direction.Down: Direction.Up,
        Direction.Left: Direction.Right,
        Direction.Right: Direction.Left
    }

    def __init__(self, map):
        self.direction = Direction.Down
        self.letters = ""
        self.steps = 0

        self.point = (self.findStart(map[0]), 0)

    def findStart(self, line):
        return line.index("|")

    def direct(self, point, direction):
        return (point[0] + direction[0], point[1] + direction[1])

    def inbound(self, point, map):
        mapHeight = len(map)
        mapWidth = len(max(m for m in map))

        return point[1] < mapHeight \
           and point[0] < mapWidth \
           and point[1] >= 0 \
           and point[0] >= 0

    def getChar(self, point, map):
        return map[point[1]][point[0]]

    def determineNewDirection(self, map):
        notLookingFor = Packet.Stop
        for direction in Direction:
            if direction == self.direction or direction == Packet.DirectionToOpposite[self.direction]:
                continue

            potentialPoint = self.direct(self.point, direction.value)
            if self.inbound(potentialPoint, map):
                potentialChar = self.getChar(potentialPoint, map)
                if potentialChar not in notLookingFor:
                    self.direction = direction
                    break

    def traverse(self, map):
        while self.inbound(self.point, map):
            x = self.point[0]
            y = self.point[1]
            currentCharacter = self.getChar(self.point, map)

            if currentCharacter.isalpha():
                self.letters += currentCharacter
            elif currentCharacter in Packet.Change:
                self.determineNewDirection(map)
            elif currentCharacter in Packet.Stop:
                break

            self.point = self.direct(self.point, self.direction.value)
            self.steps += 1

with open("input.txt", "r") as f:
    map = f.readlines()

packet = Packet(map)

packet.traverse(map)
print("Letters after traversing map are {}".format(packet.letters))
print("Steps taken: {}".format(packet.steps))

