from memory import Memory
import time

class IO:

    @staticmethod
    def read(memory, index, GUI):
        GUI.display_output("Enter number in format +/-000000:")

        GUI.prime_input()

        input = GUI.get_input()
        while input == False:
            time.sleep(0.1)
            input = GUI.get_input()

        try:
            input = int(input)
        except ValueError:
            GUI.display_error("Input must be a number")
            raise ValueError("Input must be a number")
        if (input < -999999 or input > 999999):
            GUI.display_error("Number is too large")
            raise ValueError("Number is too large")

        memory.set_main_memory(index, input)



    @staticmethod
    def write(memory, index, GUI):
        GUI.display_output("Output: " + str(memory.get_main_memory(index)).zfill(6))
