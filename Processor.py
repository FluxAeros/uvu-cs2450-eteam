from . import Memory
from . import LoadStore

class Processor:
    def process(instruction, memory):
        operationCode = int(str(instruction)[:2])

        match operationCode:
            case 10:
                #read
                pass
            
            case 11:
                #write
                pass

            case 20:
                index = int(str(instruction)[-2:])
                LoadStore.Load(index, memory)

            case 21:
                index = int(str(instruction)[-2:])
                LoadStore.Store(index, memory)

            case 30:
                #add
                pass

            case 31:
                #subtract
                pass

            case 32:
                #divide
                pass

            case 33:
                #multiply
                pass

            case 40:
                #branch
                pass

            case 41:
                #branchneg
                pass

            case 42:
                #branchzero
                pass

            case 43:
                #halt
                pass

            case default:
                raise Exception("Invalid instruction entered.")