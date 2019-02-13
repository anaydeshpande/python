def factorial(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n * factorial(n-1)

def pascal(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))


def print_triangle(rows):
    for n in range(rows +1):
        b=([pascal(n, k) for k in range(n +1)])
        print(str(b).replace('[','').replace(']','').replace(',',''))

def main():
    # Your test code here
    print_triangle(3)

if __name__ == "__main__":
    main()