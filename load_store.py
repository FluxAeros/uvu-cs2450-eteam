from memory import Memory

class LoadStore:
    @staticmethod
    def load(memory, index):
        memory.set_accumulator(memory.get_main_memory(index))

    @staticmethod
    def store(memory, index):
        memory.set_main_memory(index, memory.get_accumulator())