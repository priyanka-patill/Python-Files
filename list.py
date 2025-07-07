#first way of creation
list = [ ]
for i in range(5):
    a = int(input("Enter the elements to list\n"))
    list.append(a)
print(list)

#second way
a = [1,"Priyanka",True,3.14]
print(a)

print(type(list))
#methods
#1.append
a.append(2)
print(a)

#2.sort
list.sort()

#sort in reverse
list.sort(reverse=True)
print(list)

#index
b = a.index(3.14)

#count
print(list.count(3))

#copy
list2 = list.copy()

#insert
a.insert(2,"I")
print(a)

#extend
list2.extend(a)
print(list2)

#remove
a.remove(3.14)
print(a)

#pop
a.pop(4)
print(a)

#clear
list2.clear()
print(list2)

#operation

#concat
print(list+a)

#repetition
list*4
print(list)

#in
if ("Priyanka" in a):
    print("True\n")

else:
    print("False\n")

#not in
if ("Priyanka" not in a):
    print("True\n")

else:
    print("False\n")

#length
print(len(list))

#min
print(min(list))

#max
print(max(list))

#sum
print(sum(list))

#sorted
print(sorted(list))