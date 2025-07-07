#Develop any converter such as Rupees to dollar, temperature convertor, inch to feet etc.

#rupees to dollar
con_fact = 0.012
rupees = int(input("Enter the amoun in rupees\n"))
dollar = rupees * con_fact
print(f"The conversion of {rupees} rupees into dollar is {dollar} dollars\n")

#temp conversion
celcius = float(input("Enter the temp in celcius\n"))
far = (celcius * 9/5) + 32
print(f"The {celcius} celcius temp is equal to {far} farhenide\n")

#inch to feet
inch = int(input("Enter the length in inch\n"))
feet = inch / 12
print(f"{inch} inch is equals to {feet} feet\n")
