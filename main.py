from Memory import Memory
from ReadFile import readFileToMemory
from Processor import Processor

def main():
    memoryObj_1 = Memory()
    readFileToMemory(memoryObj_1)
    Processor.process(memoryObj_1)



if __name__ == '__main__':
    main()