# print("this is string. its is series of character which make string. And its most used data type in python ")

#to print int bettween sentence in new line,we use \n or we can do \t for tab space 
# str = "this is string. its is series of character which make string. \t And its most used data type in python"

# print(str) 

# Basic Operation

#1.contactenation

str1 = "Hello"
str2 = "World"

# print(str1+str2)
# print(str1 + " " + str2)

# in-built()
str = "Hello World"
print(len(str))

#string manipulation is not allowed
# str[2] = 'e' 

# 2.Slicing

# print(str[0: 5])
# print(str[6: len(str)])
# print(str[6: ]) #even if we dont mention last index, bydefault it will be assigned
# print(str[:5]) #even if we dont mention first index, bydefault it will be assigned

# slicing index can also be mention we negative index, negative value starting from string last char with -1 as starting index
# print(str[-5: ])
newstr= "i am Enthusiast Coder, And Learnig Python Course from Standford University"

# in-built() - check for end words
print(newstr.endswith("er"))

# only capitalize 1st char ,making rest all words 1st char in smaller
print(newstr.capitalize())

# only replace matching word with new word
print(newstr.replace("Python", "C#"))
print(newstr) #as we can use original str isn't replacedwith OP

# find() - return word 1st index
print(newstr.find("Coder"))

# count word Occurrence
str3 = "i was coder from, when i was 12 yr old"
print(str3.count("o"))





