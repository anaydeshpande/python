from test import testEqual
def sum(intList, index = 0):
    if index == 0 and len(intList) != 1:
        return intList[0] + sum(intList[1:])
    elif index == len(intList):
        return 0
    elif index < len(intList):
        return intList[index] + sum( intList, index+1)

def main():
    testEqual(sum([1,2,3]),6)
    testEqual(sum([1,2,3],3),0)
    testEqual(sum([1,2,3],2),3)

if __name__ == "__main__":
    main()