import re
from tkinter import messagebox
from memory import Memory
from tkinter.filedialog import asksaveasfile
import os

class ReadFile:
    def read_file_to_memory(memory_obj, file_path):
        convert = False
        try:
            with open(f'{file_path}', 'r+') as file:
                index = 0
                checked_convert = False
                converted_file = []

                for command in file:
                    if (len(re.sub("[^0-9]", "", command)) == 4 and checked_convert == False):
                        convert = messagebox.askyesno("Old File Conversion", "This file is in the old 4 digit format. Would you like to update and overwrite the file to 6 digits?")
                        checked_convert = True
                        if (convert):
                            numerical_command = re.sub("[^0-9]", "", command)
                            #print(numerical_command[:2])
                            sign = command[0]
                            if (numerical_command[:2] in ("10", "11", "20", "21", "30", "31", "32", "33", "40", "41", "42", "43")):
                                numerical_command = "0" + numerical_command[:2] + "0" + numerical_command[2:]
                            else:
                                numerical_command = "00" + numerical_command
                            command = sign + numerical_command
                            converted_file.append(command)
                        else:
                            memory_obj.set_main_memory(index, int(command))
                            index += 1
                    elif (len(re.sub("[^0-9]", "", command)) == 4 and convert == True):
                        numerical_command = re.sub("[^0-9]", "", command)
                        #print(numerical_command[:2])
                        sign = command[0]
                        if (numerical_command[:2] in ("10", "11", "20", "21", "30", "31", "32", "33", "40", "41", "42", "43")):
                            numerical_command = "0" + numerical_command[:2] + "0" + numerical_command[2:]
                        else:
                            numerical_command = "00" + numerical_command
                        command = sign + numerical_command
                        converted_file.append(command)
                        memory_obj.set_main_memory(index, int(command))
                        index += 1
                    elif(len(re.sub("[^0-9]", "", command)) == 4 and convert == False):
                        memory_obj.set_main_memory(index, int(command))
                        index += 1
                    elif (len(re.sub("[^0-9]", "", command)) == 6):
                        memory_obj.set_main_memory(index, int(command))
                        index += 1
                    else:
                        raise ValueError("Invalid command")
                if convert:
                    initial_filename = os.path.basename(file_path)
                    file_to_save = asksaveasfile(mode='w', defaultextension=".txt",
                                                 initialfile=initial_filename,
                                                 title="Save the converted file")
                    if file_to_save:
                        file_to_save.write("".join(converted_file))
                        file_to_save.close()

        except FileNotFoundError:
            raise FileNotFoundError("File not found")

