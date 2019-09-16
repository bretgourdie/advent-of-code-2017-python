class Shape():
    def getTransforms(self, form):
        transforms = [form]

        for i in range(3):
            previousTransform = transforms[i]

            newRotationTuples = zip(*previousTransform[::-1])
            newRotation = ["".join(list(elem)) for elem in newRotationTuples]
            transforms.append(newRotation)

        currentLength = len(transforms)
        for i in range(currentLength):
            flippedList = [l[::-1] for l in transforms[i]]

            transforms.append(flippedList)

        return transforms

    def getLineTransforms(self, transforms):
        return ["/".join(x) for x in transforms]

    def __init__(self, line):
        self.line = line
        self.form = line.split("/")
        self.size = len(self.form)
        self.transforms = self.getTransforms(self.form)
        self.allLines = self.getLineTransforms(self.transforms)

startingShape = Shape(".#./..#/###")

pass
