from Memory import Memory

class Arithmetic:
    def Add(memory, index):
        word = memory.mainMemory[index]
        memory.accumulator += word

    def Subtract(memory, index):
        word = memory.mainMemory[index]
        memory.accumulator -= word

    def Multiply(memory, index):
        word = memory.mainMemory[index]
        memory.accumulator *= word

    def Divide(memory, index):
        word = memory.mainMemory[index]
        accumulator = memory.accumulator
        memory.accumulator = int(round(accumulator/word))

