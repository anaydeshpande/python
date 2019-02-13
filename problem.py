def prime(n, d):
    a=0
    if n%d==0 and d>1:
        return a
    elif d==1:
        a +=1
        return a
    else:
        return prime(n,d-1)




def isPrime(n):
    pp = prime(n, n-1)
    return pp

def main():
    is_prime = isPrime(4)
    print is_prime

if __name__ == "__main__":
    main()

