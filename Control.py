from Memory import Memory

class Control:
    @staticmethod
    def Branch(memory, index):
        if (index >= 0 and index <= (len(memory.mainMemory)-1)):
            return index
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def BranchNeg(memory, index):
        if (index >= 0 and index <= (len(memory.mainMemory)-1)):
            if (memory.getAccumulator() < 0):
                return index
            else:
                raise Exception('The accumulator is not negative.')
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def BranchZero(memory, index):
        if (index >= 0 and index <= (len(memory.mainMemory)-1)):
            if (memory.getAccumulator == 0):
                return index
            else:
                raise Exception('The accumulator is not zero.')
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def Halt():
        return 'halt'