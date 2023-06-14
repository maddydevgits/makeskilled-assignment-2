def factorial(n):
    fact = 1
    while(n > 1):
        fact *= n
        n -= 1
    return fact
num = 5
print(factorial(num))
