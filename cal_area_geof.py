print("Program to calculate areas of diff geometric figures\n")

#circle
r = float(input("Enter the radius of circle\n"))
area_circle = 3.14 * r * r
print(f"The area of circle having radius {r} is : {area_circle}\n")

#square
side = int(input("Enter the side of square\n"))
area_square = side ** 2
print(f"The area of square having side {side} is : {area_square}\n")

#rectangle
len = int(input("Enter the length of rectangle\n"))
br = int(input("Enter the breadth of rectangle\n"))
area_rect = len * br
print(f"The area of rectangle having length {len} and breadth {br} is : {area_rect}\n")