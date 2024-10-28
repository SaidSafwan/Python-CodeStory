# Question: Write a Python program to find the common elements between two lists.

def find_common_elements(list_a, list_b):
    common_num = []
    for num in list_a:
        if list_b.count(num):
            common_num.append(num)
    return common_num


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)