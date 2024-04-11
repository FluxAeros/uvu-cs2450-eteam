import re
from tkinter import messagebox
from memory import Memory

class ReadFile:
    def read_file_to_memory(memory_obj, file_path):
        try:
            with open(f'{file_path}', 'r') as file:
                index = 0
                convert = False
                checkedConvert = False

                for command in file:
                    if(len(re.sub("[^0-9]", "", command)) == 4 and checkedConvert == False):
                        convert = messagebox.askyesno("Old File Conversion", "This file is in the old format of four digit words. Would you like to convert to the new six digit format?")
                        checkedConvert = True
                    break

                for command in file:
                    if (len(re.sub("[^0-9]", "", command)) == 4):
                        if (convert):
                            command = str(command).zfill(6)
                        memory_obj.set_main_memory(index, int(command))
                        index += 1
                    elif (len(re.sub("[^0-9]", "", command)) == 6):
                        memory_obj.set_main_memory(index, int(command))
                        index += 1
                    else:
                        raise ValueError("Invalid command")
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

