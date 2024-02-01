from Memory import Memory

class IO:
    @staticmethod
    def read(memory, index):
        if not(index >= 0 and index <= (len(memory.mainMemory)-1)):
            raise IndexError('Invalid memory location')
        
        in_num = input("Enter number in format 0000:\n")
        try:
            in_num = int(in_num)
        except:
            raise SyntaxError("input must be a number")
        if (in_num < 0 or in_num > 9999):
            raise SyntaxError("number is too large")
        
        memory.mainMemory[index] = in_num
        

    @staticmethod
    def write(memory, index):
        if (index >= 0 and index <= (len(memory.mainMemory)-1)):
            print(str(memory.mainMemory[index]).zfill(4))
        else:
            raise IndexError('Invalid memory location')