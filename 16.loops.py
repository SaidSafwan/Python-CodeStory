# while loops

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# print in reverse order
# itr = 10
# while itr >= 1:
#     print(itr)
#     itr -= 1

# print("Loop Ended")

# Qn1. Print Multiplication of n ,from 1 to 10

# n = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# Qn2. Print all element from list

# nums = [1, 3, 5, 7 , 11, 13, 17, 19, 23]

# i = 0
# while i < len(nums)-1:
#     print(nums[i])
#     i += 1
 
# ``````````````

# introducing-> break & continue statment

# nums = [1, 3, 5, 7 , 11, 13, 17, 19, 23, 11]
# x = 11
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print(nums[i], "Found at index ", i)
#         break 
#         # i += 1
#         # continue
#     else:
#         print("Finding...")
#     i += 1

# print("Loops Ended")

# `````````````

# For-Loops

# list = [1,2,3]

# for val in list:
#     print(val)

# ``````````````

# str = "HelloWorld"

# for char in str:
#     if(char == 'i'):   #if char == 'o' found, then else: code will not execute
#         break
# else:
#     print("char not found, Loop End")


# ``````````

# Range(start? Stop, step?) (? <-optional)

# for val in  range(5):  #5 us excluded
#     print(val)


# for val in  range(11,15):  #start fromm 11, 15 us excluded
#     print(val)


# for val in  range(21,30,2):  #start = 21, 30 us excluded, steps = 2
#     print(val)

# ``````

# Pass keyword

for i in range(5):
    #empty  Not allowed
    pass

print("Some Usefull work")