time = int(input("Enter the current time"))

if(time>3 and time <12):
    print("Good Morning!")
elif(time>12 and time<18):
    print("Good Afternoon!")
elif(time>18 and time<22):
    print("Good Evening!")
else:
    print("Good night!")
