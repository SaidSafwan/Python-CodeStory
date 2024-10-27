#Q1. Store following word meanings in a python dictionary :

dictItems = { 
    "table" : ["A piece of furniture", "list of figures"],
    "cat" : "a small animal"
}

print(dictItems.items())

#Q2.You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# subjects = {"python", "java", "c++" , " python", "Java" ,"c++","c","javascript"} 
# even we insert element with space / capitalize its diff element
subjects = {
     "python", "java", "c++" , "python", "java" ,"c++","c","javascript"
    }

print(len(subjects))


#q3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

std = {}

std.update({"subjects":{"phy":99, "chem": 96, "maths" : 99}})
print(std.items())


#Q4. Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types) 

set1 = set()

set1.add(9)
set1.add("9.0")

print(set1)

# OR


# # Use tuples to distinguish between int and float values
# set1.add((9, int))    # Store 9 as an integer
# set1.add((9.0, float)) # Store 9.0 as a float

# print(set1)  # Output: {(9, <class 'int'>), (9.0, <class 'float'>)}

