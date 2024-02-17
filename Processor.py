from Memory import Memory
from LoadStore import LoadStore
from Control import Control
from Arithmetic import Arithmetic
from IO import IO


class Processor:
    @staticmethod
    def process(memory):
        program_counter = 0

        while program_counter <= (len(memory.mainMemory)-1):

            instruction = memory.get_main_memory(program_counter)
            operationCode = int(str(instruction)[:2])
            index = int(str(instruction)[-2:])

            match operationCode:
                case 10:
                    IO.read(memory, index)
                    program_counter += 1
                
                case 11:
                    IO.write(memory, index)
                    program_counter += 1

                case 20:
                    LoadStore.load(memory, index)
                    program_counter += 1

                case 21:
                    LoadStore.store(memory, index)
                    program_counter += 1

                case 30:
                    Arithmetic.add(memory, index)
                    program_counter += 1

                case 31:
                    Arithmetic.subtract(memory, index)
                    program_counter += 1

                case 32:
                    Arithmetic.divide(memory, index)
                    program_counter += 1

                case 33:
                    Arithmetic.multiply(memory, index)
                    program_counter += 1

                case 40:
                    program_counter = Control.branch(memory, index)

                case 41:
                    newIndex = Control.branch_neg(memory, index)
                    if (newIndex == 'no_branch'):
                        program_counter += 1
                    else:
                        program_counter = newIndex

                case 42:
                    newIndex = Control.branch_zero(memory, index)
                    if (newIndex == 'no_branch'):
                        program_counter += 1
                    else:
                        program_counter = newIndex

                case 43:
                    break

                case default:
                    raise Exception("Invalid instruction entered.")