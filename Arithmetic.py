from Memory import Memory

class Arithmetic:
    def add(memory, index):
        word = memory.mainMemory[index]
        memory.accumulator += word

    def subtract(memory, index):
        word = memory.mainMemory[index]
        memory.accumulator -= word
