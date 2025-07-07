def mean(a,b):
    calculate = (a+b)/2
    print(f"The mean of {a} and {b} is : {calculate}\n")

def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact * i 
        i+1
    print(f"The factorial of {n} is {fact}\n")

x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))

mean(x,y)
factorial(x)