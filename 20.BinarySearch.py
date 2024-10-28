def BinarySearch(arr, start, end, target):
    if start > end:
        return -1
    
    while start <= end:
        mid = (start + end)// 2
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

arr = [1, 4, 5, 6, 8, 10, 12, 14, 15]
print(BinarySearch(arr, 0, len(arr) - 1, 15))


# Note: to learn
# Using / division:
# mid = (start + end) / 2    # This would give a float result, like 4.5

# Using // division:
# mid = (start + end) // 2   # This would give an integer result, like 4
