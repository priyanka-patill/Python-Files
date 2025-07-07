Num = int(input("Enter the number: "))
fact = 1
for i in range(Num,0,-1):
    fact = fact * i
    
print(f"The factorial of {Num} is",fact)
