BS = int(input("Enter the basic salary of employee\n"))

DA = BS * (70/100)

TA = BS * (30/100)

HRA = BS * (10/100)

result = BS + DA + TA + HRA 
print(f"The gross salary of employee is {result}\n")