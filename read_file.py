from memory import Memory

class ReadFile:
    def read_file_to_memory(memory_obj, file_path):
        try:
            file = open(f'{file_path}', 'r')
            index = 0
            for command in file:
                if (len(command) == 4):
                    memory_obj.set_old_file(True)
                    #command = str(command).zfill(6)
                    memory_obj.set_main_memory(index, int(command))
                    index += 1
                elif (len(command) == 6):
                    memory_obj.set_main_memory(index, int(command))
                    index += 1
                else:
                    raise ValueError("Invalid command")
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

