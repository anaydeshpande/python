from test import testEqual
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def main():
    testEqual(gcd(6, 9), 3)


if __name__ == "__main__":
    main()