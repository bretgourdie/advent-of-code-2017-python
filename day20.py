class DeleteCollisions():
    def __init__(self):
        self.removeCollisions = True

class IgnoreCollisions():
    def __init__(self):
        self.removeCollisions = False

class Simulation():
    def run(self, input, collisionStrategy):
        particles = []
        for i, line in enumerate(lines):
            particles.append(Particle(i, line))

        currentWinner = CurrentWinner()

        while currentWinner.rounds < 300:
            for particle in particles:
                particle.update()

            if collisionStrategy.removeCollisions:
                positionToParticle = {}

                for particle in particles:
                    if particle.p not in positionToParticle:
                        positionToParticle[particle.p] = []
                    positionToParticle[particle.p].append(particle)

                for position in positionToParticle:
                    pParticles = positionToParticle[position]
                    if len(pParticles) > 1:
                        for particle in pParticles:
                            particle.markedForDeletion = True

                particles = [p for p in particles if not p.markedForDeletion]

            winner = min(particles, key=lambda p: p.getDistance())
            currentWinner.set(winner)


        withOrWithout = "with" + "out" if not collisionStrategy.removeCollisions else ""
        print("Particle that will stay closest to 0,0,0 {} collisions is {}".format(withOrWithout, currentWinner.particle.number))

class Point3D():
    def __init__(self, x: str, y: str, z: str):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __key(self):
        return (self.x, self.y, self.z)

    def __hash__(self):
        return hash(self.__key())

class Particle():
    def __init__(self, number: int, line: str):
        self.number = number
        self.p, self.v, self.a = [Point3D(*s[s.index("<")+1:s.index(">")].split(",")) for s in line.split(", ")]
        self.markedForDeletion = False

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

    def isColliding(self, other):
        return self.p == other.p

    def __eq__(self, other):
        return self is not None and other is not None and self.number == other.number

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

Simulation().run(lines, IgnoreCollisions())
Simulation().run(lines, DeleteCollisions())
