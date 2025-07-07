print("Let's play Kon Banega Crorepati!!\n")
print("Can we start the game??")
gamer_choice = input("Enter yes or no\n")
    
if(gamer_choice == "yes"):
    amount=0
    question = ("Which method is not applicable for tuple?\n")
    print(question)
    option = ("a)append b)index c)sort d)count")
    print(option)
    answer = input("Enter the option\n")
    if(answer == "a"):
        print("Correct answer!")
        amount = amount + 1000
    else:
        print("Wrong answer! Better luck next time")
    print(f"Game over! You have won {amount} rupees")

else:
    print("Exiting from the game!")
