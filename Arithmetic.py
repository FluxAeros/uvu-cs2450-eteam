from memory import Memory

class Arithmetic:
    @staticmethod
    def add(memory, index):
        word = memory.get_main_memory(index)
        memory.set_accumulator(memory.get_accumulator() + word)

    @staticmethod
    def subtract(memory, index):
        word = memory.get_main_memory(index)
        memory.set_accumulator(memory.get_accumulator() - word)

    @staticmethod
    def multiply(memory, index):
        word = memory.get_main_memory(index)
        memory.set_accumulator(memory.get_accumulator() * word)

    @staticmethod
    def divide(memory, index):
        word = memory.get_main_memory(index)
        memory.set_accumulator(int(round(memory.get_accumulator() / word)))

