from Memory import Memory

class IO:
    @staticmethod
    def Read(memory: Memory(), index: int):
        in_num = input("Enter number in format +/-0000:\n")
        try:
            in_num = int(in_num)
            print(in_num)
        except:
            raise SyntaxError("input must be a number")
        if (in_num < -9999 or in_num > 9999):
            raise OverflowError("number is too large")
        
        memory.mainMemory[index] = in_num
        

    @staticmethod
    def Write(memory: Memory(), index: int):
        print(str(memory.mainMemory[index]).zfill(4))