# Question 9: Write a Python program to find the second largest number in a list.

def find_second_Largest(numbers):
    nums.sort()
    # print(nums)
    return nums[len(nums)-2]

    # OR

# def find_second_Largest(numbers):
#     largest = float('-inf')
#     second_largest = float('-inf')
#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif  num > second_largest and num != largest:
#             second_largest = num
#     return second_largest

nums = [1 , 5, 2, 4, 5, 7, 9, 8 ,6]
second_largest = find_second_Largest(nums)
print(f"second largest number is {second_largest}")

