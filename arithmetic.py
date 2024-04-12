from memory import Memory

class Arithmetic:
    @staticmethod
    def overflow(ans):
        # Convert the number to string to easily manipulate digits
        ans_str = str(abs(ans))
        if len(ans_str) > 6:
            # Truncate to last six digits
            truncated_ans = ans_str[-6:]
            return int(truncated_ans) if ans >= 0 else -int(truncated_ans)
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
