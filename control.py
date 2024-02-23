from memory import Memory

class Control:
    @staticmethod
    def branch(memory, index):
        if (index >= 0 and index <= (len(memory.main_memory)-1)):
            return index
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def branch_neg(memory, index):
        if (index >= 0 and index <= (len(memory.main_memory)-1)):
            if (memory.get_accumulator() < 0):
                return index
            else:
                return 'no_branch'
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def branch_zero(memory, index):
        if (index >= 0 and index <= (len(memory.main_memory)-1)):
            if (memory.get_accumulator() == 0):
                return index
            else:
                return 'no_branch'
        else:
            raise IndexError('The memory location does not exist.')

    @staticmethod
    def halt():
        return 'halt'
