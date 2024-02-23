from memory import Memory
import threading

class IO:
    
    input_ready_event = threading.Event()
    @staticmethod
    def read(memory, index, GUI):
        IO.input_ready_event.clear()
        GUI.display_output("Enter number in format +/-0000:")
        IO.input_ready_event.wait()
        in_num = GUI.user_input
        try:
            in_num = int(in_num)
        except:
            GUI.display_error("Input must be a number")
            raise SyntaxError("Input must be a number")
        if (in_num < -9999 or in_num > 9999):
            GUI.display_error("Number is too large")
            raise OverflowError("Number is too large")
        
        memory.set_main_memory(index, in_num)
        

    @staticmethod
    def write(memory, index, GUI):
        GUI.display_output("Output: " + str(memory.get_main_memory(index)).zfill(4))
