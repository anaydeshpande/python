def factorial(x):

    return 1 if x == 0 else x * factorial(x - 1)

def triangle(n):

    return [[factorial(i) / (factorial(j) * factorial(i - j)) for j in range(i + 1)] for i in range(n)]

print triangle(4)