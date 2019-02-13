def square(n):
    # Your recursive code here
    if n ==1:
        return 1
    if n > 1:
        return square(n-1) + (2 * n) - 1

def cube(n):
    #Your code here
    if n ==1:
        return 1
    if n > 1:
        return (cube(n-1) + (3 * square(n)) - (3 * n) + 1)

def main():
# Your test code here
    print cube(5)

if __name__ == "__main__":
    main()
