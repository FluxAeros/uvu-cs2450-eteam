from memory import Memory

class IO:
    @staticmethod
    def read(memory, index):
        in_num = input("Enter number in format +/-0000:\n")
        try:
            in_num = int(in_num)
        except:
            raise SyntaxError("Input must be a number")
        if (in_num < -9999 or in_num > 9999):
            raise OverflowError("Number is too large")
        
        memory.set_main_memory(index, in_num)
        

    @staticmethod
    def write(memory, index):
        print(str(memory.get_main_memory(index)).zfill(4))