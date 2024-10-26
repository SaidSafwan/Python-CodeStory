mark1 = 94.5
mark2 = 87.8
mark1 = 78.9
mark1 = 82.7

marks = [94.5, 87.8, 78.9, 82.7, 56.8]
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[4])

# print(marks[8]) #error out of range


# we can also include diff data types in list
student= ["said",22, 98.9, "class-a", "Athlete"]
# print(student)

# NOTE: list are Mutable (Changeable) | string are immutable(Non-Changeable)

#slicing
# print(student[0: 3])

# list method

list = [2, 1 , 3]
list.append(4)
print(list)

list.sort()
# list(list.sort())  #if we do o/p will be None, as list = list.sort() doesn't return back anything, so o.p will be None 
print(list)

# list.sort(reverse=True)
# print(list)

# OR

# list.reverse()
# print(list)

list.insert(1, 5)
print(list)

# list.remove(5) #id multiple present then will remove 1st Occurrence
# print(list)

# or

list.pop(1)
print(list)





