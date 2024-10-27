# element are stored in unordered style
# each element in the set must be unique & immutable - (so we can't us set in list/dict)

# NOTE SET ARE mutable  (can add/remove element) | each element in set are immutable (can't element like list[] which r (mutable)changable )

collection = {1, 2, 2, 2, "Hello", "world", 4} #duplicate ignored

# print(collection)
# print(type(collection))
# print(len(collection))

# new_collecion = {} #this creat empty dictionary
# print(type(new_collecion))

# to creat empty set syntax
new_collection = set()
# print(type(new_collection))

# methods

# 1.add()

new_collection.add(1)
new_collection.add(2)
new_collection.add("Hello")
new_collection.add(("Python", "C++", "Java"))
new_collection.add(2)

# print(new_collection)

# 2.remove() | remove element

new_collection.remove(1)
# print(new_collection)

# print(new_collection.remove(6))  #Error 

# 3.clear()

new_collection.clear()
# print(new_collection)

# 4.pop() - will pop random element 
# print(new_collection.pop())

# print(new_collection)

#Union 

set1 = {1, 2, 3}
set2 = {2, 3, 5}

print("Union Elements: ",set1.union(set2))
print(set1)
print(set2)

#Intersection

print("Intersection Elements: ", set1.intersection(set2))
print(set1)
print(set2)