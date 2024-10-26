# variables

name = "Said"
age = -23
salary = 60.58

# print(name)
# print(age)
# print(salary)

isEmployer = True
a = None
# Data Types

# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(isEmployer))
# print(type(a))


# arithmetic operator
# a = 10
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) #alway result in float
# print(a % b) #Modulo
# print(a ** b)  #power a ^ b


#relational operator
# a = 50
# b = 40

# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)
# print(a > b)
# print(a < b)

#Assignment Opertor 

# num = 10
# num = num + 10
# num += 10   #short-hand
# print(num)
# num -= 10   
# num *= 10   
# num /= 5   
# num %= 5   
# num **= 5   
# print(num)

#logical operator

# print(not True)
# print(not False)

# a = 90 
# b = 40

# print(not (a < b))

# val1 = True
# val2 = True

# print("AND operator :" , val1 and val2)
# val2 = False
# print("AND operator :" , val1 and val2)

# print("OR operator :" , val1 or val2)

# Type Converion (Auto done by Compiler) & Type casting

a = 2
b = 4.25

sum = a + b
#here a (int) is converted to float, to result in flaoting value as b which is aleready has flat value, and float vlaue are superior with extra information. so int 2 get converted to 2.0 float value. so this kind of convertion are type conversion

# a = "2"
# sum = a + b #will trow error, 
a = int("2") #implicit type casting
sum = a + b
print(sum)
