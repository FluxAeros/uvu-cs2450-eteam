from memory import Memory

class ReadFile:
    def read_file_to_memory(memory_obj, file_path):
        try:
            file = open(f'{file_path}', 'r')
            index = 0
            for command in file:
                memory_obj.set_main_memory(index, int(command))
                index += 1
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

