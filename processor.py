from memory import Memory
from load_store import LoadStore
from control import Control
from arithmetic import Arithmetic
from input_output import IO


class Processor:
    @staticmethod
    def process(memory, GUI):
        program_counter = 0

        while program_counter <= (len(memory.main_memory)-1):

            instruction = memory.get_main_memory(program_counter)
            operationCode = int(str(instruction)[:2])
            index = int(str(instruction)[-2:])

            match operationCode:
                case 10:
                    IO.read(memory, index, GUI)
                    program_counter += 1

                case 11:
                    IO.write(memory, index, GUI)
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
                    GUI.toggle_run()
                    break

                case default:
                    raise Exception("Invalid instruction entered.")
