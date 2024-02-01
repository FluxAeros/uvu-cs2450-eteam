import Memory


# We can move this func to another location if we feel the main file is too cluttered
# We could also move all these operations into a object for simplicity
def doOperations(Operation, location):
    if Operation == 10:
        print("Read OPP")
        print(Operation, location)
        # readOpp(location)
    elif Operation == 11:
        print("write Opp")
        print(Operation, location)
        # writeOpp(location)
    elif Operation == 20:
        print("load Opp")
        print(Operation, location)
        # loadOpp(location)
    elif Operation == 21:
        print("store Opp")
        print(Operation, location)
        # loadOpp(location)
    elif Operation == 30:
        print("add opp")
        # addOpp(location)
    elif Operation == 31:
        print("sub opp")
        # subOpp(location)
    elif Operation == 32:
        print("divide opp")
        # divideOpp(location)
    elif Operation == 33:
        print("Multi opp")
        # multiOpp(location)
    elif Operation == 40:
        print("Branch opp")
        # branchOpp(location)
    elif Operation == 41:
        print("BranchNeg opp")
        # branchNegOpp(location)
    elif Operation == 42:
        print("BranchZero opp")
        # multiOpp(location)
    elif Operation == 43:
        print("halt opp")
        # haltOpp()
    else:
        print("Operation not found")


def main():
    file = input("Enter the name of your file, if not running a file hit enter: ")
    if file:
        try:
            file = open(f'TestFiles/{file}', 'r')
            for command in file:
                opp = int(command[1:3])
                loc = int(command[3:5])
                doOperations(opp, loc)
        except FileNotFoundError:
            print("File not found")
    else:
        comm = ""
        while comm != "STOP":
            # Input need to be in the same 5 char format as the text doc, IE "+1001"
            comm = input("Enter your commands, Enter STOP to stop ")
            if comm == "STOP":
                break
            opp = int(comm[1:3])
            loc = int(comm[3:5])
            doOperations(opp, loc)


if __name__ == '__main__':
    main()

