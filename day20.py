class Point3D():
    def __init__(self, x: str, y: str, z: str):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

class Particle():
    def __init__(self, number: int, line: str):
        self.number = number
        self.p, self.v, self.a = [Point3D(*s[s.index("<")+1:s.index(">")].split(",")) for s in line.split(", ")]

    def add(self, point3dA: Point3D, point3dB: Point3D):
        return Point3D(
            point3dA.x + point3dB.x,
            point3dA.y + point3dB.y,
            point3dA.z + point3dB.z)

    def update(self):
        self.v = self.add(self.v, self.a)
        self.p = self.add(self.p, self.v)

    def getDistance(self):
        return abs(self.p.x) + abs(self.p.y) + abs(self.p.z)

class CurrentWinner():
    def __init__(self):
        self.particle = None
        self.rounds = 0

    def set(self, particle: Particle):
        if self.particle == particle:
            self.rounds += 1
        else:
            self.particle = particle
            self.rounds = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

particles = []
for i, line in enumerate(lines):
    particles.append(Particle(i, line))

currentWinner = CurrentWinner()

while currentWinner.rounds < 300:
    for particle in particles:
        particle.update()

    winner = min(particles, key=lambda p: p.getDistance())
    currentWinner.set(winner)

print("Particle that will stay closest to 0,0,0 is {}".format(currentWinner.particle.number))
