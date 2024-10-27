# Wap To check if list contains a plaindrome of elements

list1 = [1,2,3]
list2 = ["r", "a", "c", "e", "c", "a", "r"]

# copy_list1 = list1.copy()
# copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if(list2 == copy_list2):
    print("Palindrome")
else:
    print("Not Palindrome")



# WAP to print count of elment from tuple


Grade = ["A","C", "D", "B","A", "C", "B"]

print(Grade.count("A"))


# WAP to sort the element from list
Grade = ["A","C", "D", "B","A", "C", "B"]

Grade.sort()
print(Grade)


