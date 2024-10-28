def InsertionSort(arr, n):
    for i in range(1, n):  # Start from 1, as the first element is "sorted"
        element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > element:  # Change to > for ascending order
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element  # Insert element in the correct position

n = int(input("Enter list size: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))  # Convert input to integer

InsertionSort(arr, n)
print("Sorted list:", arr)


# def InsertionSort(arr, n):
#     for i in range(1, n):
#         Element = arr[i]
#         # print("current element is:", arr[i],end =" ")
#         j = i - 1
#         for j in range(j, -2, -1):
#             print("value of j :", j)
#             if arr[j] > Element:
#                 arr[j + 1] = arr[j]  # Shift element to the right
#                 # print("After swap current list:", arr, "also index of j is :", j)
#             else:
#                 break
#         arr[j+1] = Element      # Place Element in its sorted position
#         # print("current list:", arr)

# n = int(input("Enter list size: "))
# arr = []
# for i in range(n):
#     arr.append(int(input()))  # Convert input to integer

# InsertionSort(arr, n)
# print("Sorted list:", arr)

