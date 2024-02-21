from memory import Memory

class Arithmetic:
    @staticmethod
    def overflow(ans):
        #checking for overflow
        length = len(str(ans))
        #accounting for '-' sign
        neg = False
        if ans < 0:
            neg = True
        if length > 4:
            overflow = length - 4
            #converting ans to string for truncation
            if neg:
                return int(str(ans)[overflow:]) * -1
            else:
                return int(str(ans)[overflow:])
        else:
            return ans

    def Add(memory, index):
        word = memory.get_main_memory(index)
        ans = memory.get_accumulator() + word
        memory.set_accumulator(Arithmetic.overflow(ans))
        
    def Subtract(memory, index):
        word = memory.get_main_memory(index)
        ans = memory.get_accumulator() - word
        memory.set_accumulator(Arithmetic.overflow(ans))

    def Multiply(memory, index):
        word = memory.get_main_memory(index)
        ans = memory.get_accumulator() * word
        memory.set_accumulator(Arithmetic.overflow(ans))

    def Divide(memory, index):
        word = memory.get_main_memory(index)
        ans = int(round(memory.get_accumulator() / word))
        memory.set_accumulator(Arithmetic.overflow(ans))
