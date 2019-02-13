#from test import testEqual
def fib(n):
    # Your recursive code here
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    # Your test code here
    #testEqual(fib(3),2)
    print(fib(12))

if __name__ == "__main__":
    main()