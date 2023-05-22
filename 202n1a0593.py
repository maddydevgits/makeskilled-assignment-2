#recursion function
def factorial(x):
 if x==0 or x==1:
    return 1
 else:
   fact=x * factorial(x-1)
   return fact
 
 n = int(input("enter a number:"))
 print(f"factorial of number {n}! is {factorial(n)}")
 
