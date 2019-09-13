class Shape():
    def getTransforms(self, form):
        transforms = [form]

        for i in range(3):
            # fix rotations
            pass

        flippedList = [l[::-1] for l in form]

        transforms.append(flippedList)

        return transforms

    def __init__(self, line):
        self.form = line.split("/")
        self.size = len(self.form)
        self.transforms = self.getTransforms(self.form)

startingShape = Shape(".#./..#/###")

print(startingShape.form)
