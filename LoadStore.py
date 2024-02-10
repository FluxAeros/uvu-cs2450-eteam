from Memory import Memory

class LoadStore:
    @staticmethod
    def Load(memory, index):
        memory.setAccumulator(memory.getMainMemory(index))

    @staticmethod
    def Store(memory, index):
        memory.setMainMemory(index, memory.getAccumulator())