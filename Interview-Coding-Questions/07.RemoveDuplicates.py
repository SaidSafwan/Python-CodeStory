# Question: Write a Python program to remove duplicates from a list.


# def remove_duplicates(numbers):
#     for num in numbers:
#         while numbers.count(num) > 1:
#             numbers.remove(num)
#     return numbers

# Optimized Approach

def remove_duplicates(numbers):
    unique_nums = []
    for num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums


# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(unique_nums)