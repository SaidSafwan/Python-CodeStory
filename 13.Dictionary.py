info = {
    "name" : "Said",
    "Subjects": ["python", "C++", "Java"],
    "topics" : ("disct", "set"),
    "age" : 35,
    "role" : "SDE",
    12.99 : 94.4
} 

# info["name"] = "Alex" #overwrite
# info["Surname"] = "costa" #will create new key values
# print(info)
# print(type(info))

# null_dict = {}
# null_dict["name"] = "CodeBender"
# print(null_dict)



#NESTED Dictionary: inset value as dictionary, inside dictionary.
student = {
    "Name" : "rohan kumar",
    "class" : "A",
    "subjects" : {
        "phy" : 98, 
        "chem" : 97,
        "maths" : 98
    },
    "class" : "A",
    "gender" : "male"
}

# here class is inserted twice but still considered only key, reason: Duplicate keys not allowed

student["class"] = "B" #will update key value , [avoid duplicate]


# print(student["subjects"])
# print(student["subjects"]["phy"])


# methods

# 1. to print all keys
# print(student.keys())

# type casting all dictionary key to list

# print("list format of keys: ", list(student.keys()))
# print("tuple format of keys: ", tuple(student.keys()))

# length 
# print("length : ",len(list(student.keys())) )

#2. to print all value of dictionary
# print(student.values())

# we can also type cast this value into list and tuple
# print("list format of values: ", list(student.values()))
# print("tuple format of values: ", tuple(student.values()))


# 3. To print all item[key:value] from dictionary

# print(student.items())

# pairs = list(student.items())  #we can also acces with list
# print(pairs[0])  #ill print 1st item[key:value]

# 4. To Return Key according Value

print(student["Name"])
# print(student["name"])   #as we dont have key as name, will throw ERROR & Stop exec

# or 

print(student.get("Name"))  
# print(student.get("name")) #but it get will return NONE , & continue execution

# 5. insert specific item into dictionary

student["phone_no"] = 9999888807  #mutable(changable)
# OR

print(student.update({"city":"Wall of street"}))
# OR
new_dict = {"Country": "USA " }

student.update(new_dict)

print(student)