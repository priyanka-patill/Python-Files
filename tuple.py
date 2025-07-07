#first way of creation
tup = ( )

#need to convert it into list
list2 = list(tup)
for i in range(5):
    a = int(input("Enter the elements to list2\n"))
    list2.append(a)

tup = tuple(list2)
print(tup)

#second way
a = (1,"Priyanka",True,3.14)
print(a)

print(type(tup))
#methods

#to perform any operation or to apply any method first covert tuple into list

#1.append
list2 = list(tup)
list2.append(2)
tup = list(list2)
print(tup)

#2.sort
tup.sort()
print(tup)

#sort in reverse
tup.sort(reverse=True)
print(tup)

#index
b = a.index(3.14)

#count
print(tup.count(3))

#copy
tup2 = tup.copy()

#insert
b = list(a)
b.insert(2,"I")
a = tuple(b)
print(a)

#extend
list2 = list(tup)
list2.extend(a)
tup = tuple(list2)
print(tup)

#remove
b = list(a)
b.remove(3.14)
a = tuple(b)
print(a)

#clear
tup2.clear()
print(tup2)