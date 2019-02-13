from test import testEqual
def prime(n, d):
    # p =0 means its not prime number and p =1 means its a prime number
    p = 0
    if d> 1 and (n % d) == 0:
        return p
    elif d ==1:
        p += 1
        return p
    else:
        return prime(n, d - 1)


def isPrime(n):
    #Your code here
    pp = prime(n, n-1)
    return pp

def main():
    # Your test code here
    testEqual(isPrime(5), 1)


if __name__ == "__main__":
    main()