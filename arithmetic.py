from memory import Memory

class Arithmetic:
    @staticmethod
    def overflow(ans):
        length = len(str(abs(ans)))
        if length > 6:
            overflow = length - 6
            ans_str = str(ans)
            truncated_ans = ans_str[0] + ans_str[overflow+1:] if ans < 0 else ans_str[overflow:]
            return int(truncated_ans)
        else:
            return ans

    def add(memory, index):
        word = memory.get_main_memory(index)
        ans = memory.get_accumulator() + word
        memory.set_accumulator(Arithmetic.overflow(ans))
        
    def subtract(memory, index):
        word = memory.get_main_memory(index)
        ans = memory.get_accumulator() - word
        memory.set_accumulator(Arithmetic.overflow(ans))

    def multiply(memory, index):
        word = memory.get_main_memory(index)
        ans = memory.get_accumulator() * word
        memory.set_accumulator(Arithmetic.overflow(ans))

    def divide(memory, index):
        word = memory.get_main_memory(index)
        ans = int(round(memory.get_accumulator() / word))
        memory.set_accumulator(Arithmetic.overflow(ans))
