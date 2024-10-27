# tuple are similiar to string , which is immutable, 
# similiar to list instead of [], tuple are enclosed with (ele,)
tup = (1, 4, 8 , 1, 9, 3, 1)

print(type(tup))
print(tup[3])
print(tup[4])

# tup[0] = 5  #Not Allowed

# to find index of 1st occurrence o matching element
print(tup.index(4))

# count the occurrence of element in tuple
print(tup.count(1))

# slicing 

print(tup[:3])


