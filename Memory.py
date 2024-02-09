class Memory:
    def __init__(self):
        self.mainMemory = [0] * 100
        self.accumulator = 0

    def getMainMemory(self, index):
        try:
            return self.mainMemory[index]
        except IndexError:
            raise IndexError('The memory location does not exist.')

    def setMainMemory(self, index, value):
        try:
            self.mainMemory[index] = value
        except IndexError:
            raise IndexError('The memory location does not exist.')

    def getAccumulator(self):
        return self.accumulator

    def setAccumulator(self, value):
        self.accumulator = value