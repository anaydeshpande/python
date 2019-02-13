from test import testEqual
def palindrome(aString):
    # Your recursive code here
    if aString == "":
        return True
    elif len(aString) == 1:
        return True
    elif aString[0] == aString[-1]:
        return palindrome(aString[1:-1])
    elif aString[0] != aString[-1]:
        return False
    else:
        aString == aString[::-1]
        return True

def main():
    # Your test code here
    testEqual(palindrome(""),True)
    testEqual(palindrome("a"),True)
    testEqual(palindrome("a"+"AbbA"+"a"),True)
    testEqual(palindrome("a"+"AbbA"+"b"),False)

if __name__ == "__main__":
    main()