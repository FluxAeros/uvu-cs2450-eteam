from Memory import Memory
from ReadFile import readFileToMemory
from Processor import Processor
from gui import GUI

def main():
    gui = GUI()
    memoryObj_1 = Memory()
    readFileToMemory(memoryObj_1)
    Processor.process(memoryObj_1)

if __name__ == '__main__':
    main()