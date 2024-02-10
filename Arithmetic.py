from Memory import Memory

class Arithmetic:
    def Add(memory, index):
        word = memory.getMainMemory(index)
        memory.setAccumulator(memory.getAccumulator() + word)

    def Subtract(memory, index):
        word = memory.getMainMemory(index)
        memory.setAccumulator(memory.getAccumulator() - word)

    def Multiply(memory, index):
        word = memory.getMainMemory(index)
        memory.setAccumulator(memory.getAccumulator() * word)

    def Divide(memory, index):
        word = memory.getMainMemory(index)
        memory.setAccumulator(int(round(memory.getAccumulator() / word)))

