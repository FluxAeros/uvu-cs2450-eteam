class Memory:
    def __init__(self):
        self.main_memory = [0] * 250
        self.accumulator = 0

    def get_main_memory(self, index):
        try:
            return self.main_memory[index]
        except IndexError:
            raise IndexError('The memory location does not exist.')

    def set_main_memory(self, index, value):
        try:
            self.main_memory[index] = value
        except IndexError:
            raise IndexError('The memory location does not exist.')

    def get_accumulator(self):
        return self.accumulator

    def set_accumulator(self, value):
        self.accumulator = value
