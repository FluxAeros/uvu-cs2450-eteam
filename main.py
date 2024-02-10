from Memory import Memory
from readFile import readFileToMemory
from Processor import processor

def main():
    memoryObj_1 = Memory()
    readFileToMemory(memoryObj_1)
    Processor.process(memoryObj_1.mainMemory)



if __name__ == '__main__':
    main()

