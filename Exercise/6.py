from test import testEqual
def square(n):
    if n ==1:
        return 1
    if n > 1:
        return square(n-1) + (2 * n) - 1

def cube(n):
    if n ==1:
        return 1
    if n > 1:
        return (cube(n-1) + (3 * square(n)) - (3 * n) + 1)

def main():
    testEqual(square(5),25)
    testEqual(cube(5),125)
    testEqual(square(5)+cube(5),150)

if __name__ == "__main__":
    main()