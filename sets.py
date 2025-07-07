CET = {"Priyanka", "Manav", "Aniket", "Pooja", "Saarthak", "Tushar", "Bhavesh", "Aaditya", "Mayur", "Aashish", "Krishna"}
JEE = {"Priyanka", "Manav", "Aniket", "Pooja"}
NEET = {"Bhavesh", "Saarthak", "Aniket", "Mayur", "Tushar", "Vishwajit"}

#union
union = CET | JEE | NEET
print(f"The number of students and names who have attempted atleast one exam are {len(union),union}\n")

print(f"The number of students and names who have attempted only CET and JEE{CET | JEE,len(CET | JEE )}\n")

print(f"The number of students and names who have attempted only CET and NEET{CET | NEET,len(CET | NEET )}\n")

print(f"The number of students and names who have attempted only NEET and JEE{NEET | JEE,len(NEET | JEE )}\n")

#intersection
print(f"The number of students and names who have attempted all the exams are {CET & JEE & NEET, len(CET & JEE & NEET)}\n")
print(f"The number of students and names who have attempted both CET and JEE are {CET & JEE , len(CET & JEE)}\n")
print(f"The number of students and names who have attempted both CET and NEET are {CET & NEET, len(CET & NEET)}\n")
print(f"The number of students and names who have attempted both JEE and NEET are {JEE & NEET, len(JEE & NEET)}\n")

#difference
print(f"The number of students and names who have attempted CET but not JEE and NEET are {CET - JEE - NEET, len(CET - JEE - NEET)}\n")
print(f"The number of students and names who have attempted CET but not JEE are {CET - JEE , len(CET - JEE)}\n")
print(f"The number of students and names who have attempted CET but not NEET are {CET - NEET, len(CET - NEET)}\n")
print(f"The number of students and names who have attempted JEE but not NEET are {JEE - NEET, len(JEE - NEET)}\n")