from Memory import Memory

class LoadStore:
    @staticmethod
    def Load(index, memory):
        try:
            memory.accumulator = memory.mainMemory[index]
        except IndexError:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def Store(index, memory):
        try:
            memory.mainMemory[index] = memory.accumulator
        except IndexError:
            raise IndexError('The memory location does not exist.')