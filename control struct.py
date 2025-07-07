# Conditional Statements
number = 10
if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# For Loop
for i in range(5):   
    print(i)

# While Loop
counter = 3
while counter > 0:
    print(counter)
    counter -= 1

for i in range(5):
    if i == 2:
        continue  
    if i == 4:
        break  
    print(f"Value: {i}")
