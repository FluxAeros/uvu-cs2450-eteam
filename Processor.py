from Memory import Memory
from LoadStore import LoadStore
from Control import Control
from Arithmetic import Arithmetic
from IO import IO


class Processor:
    @staticmethod
    def process(memory):
        programCounter = 0

        while programCounter <= (len(memory.mainMemory)-1):

            instruction = memory.getMainMemory(programCounter)
            operationCode = int(str(instruction)[:2])
            index = int(str(instruction)[-2:])

            match operationCode:
                case 10:
                    IO.Read(memory, index)
                    programCounter += 1
                
                case 11:
                    IO.Write(memory, index)
                    programCounter += 1

                case 20:
                    LoadStore.Load(memory, index)
                    programCounter += 1

                case 21:
                    LoadStore.Store(memory, index)
                    programCounter += 1

                case 30:
                    Arithmetic.Add(memory, index)
                    programCounter += 1

                case 31:
                    Arithmetic.Subtract(memory, index)
                    programCounter += 1

                case 32:
                    Arithmetic.Divide(memory, index)
                    programCounter += 1

                case 33:
                    Arithmetic.Multiply(memory, index)
                    programCounter += 1

                case 40:
                    programCounter = Control.Branch(memory, index)

                case 41:
                    newIndex = Control.BranchNeg(memory, index)
                    if (newIndex == 'noBranch'):
                        programCounter += 1
                    else:
                        programCounter = newIndex

                case 42:
                    newIndex = Control.BranchZero(memory, index)
                    if (newIndex == 'noBranch'):
                        programCounter += 1
                    else:
                        programCounter = newIndex

                case 43:
                    break

                case default:
                    raise Exception("Invalid instruction entered.")