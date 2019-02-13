def palindrome(aString):
    # Your recursive code here
    if aString == "":
        return True
    if len(aString) == 1:
        return True

def main():
    # Your test code here
    print palindrome("a")

if __name__ == "__main__":
    main()