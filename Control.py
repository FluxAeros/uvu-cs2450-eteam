from Memory import Memory

class Control:
    @staticmethod
    def Branch(memory, index):
        if (index >= 0 and index <= len(memory.mainMemory)):
            return index
        else:
            raise 

    @staticmethod
    def BranchNeg(memory, index):
        if (index >= 0 and index <= len(memory.mainMemory) and memory.accumulator < 0):
            return index
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def BranchZero(memory, index):
        if (index >= 0 and index <= len(memory.mainMemory) and memory.accumulator == 0):
            return index
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def Halt():
        pass