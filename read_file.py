class ReadFile:
    def read_file_to_memory(memory_obj):
        print("If you want to enter your own commands press enter.")
        file = input("Enter in the name of the file you would like to use: ")
        
        if file:
            try:
                file = open(f'RunCommands/{file}', 'r')
                index = 0
                for command in file:
                    memory_obj.set_main_memory(index, int(command))
                    index += 1
            except FileNotFoundError:
                raise FileNotFoundError("File not found")
        else:
            comm = ""
            index = 0
            while comm != "STOP":
                comm = input("Enter your commands, Enter STOP to stop ")
                if comm == "STOP":
                    break
                else:
                    memory_obj.set_main_memory(index, int(comm))
                    index += 1

