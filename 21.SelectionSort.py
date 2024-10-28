def SelectionSort(list, n):
    for i in range(n-1):
        small_element = list[i]
        index = i
        for j in range(i+1, n):
            if(list[j] < small_element):
                small_element = list[j]
                index = j
        if(small_element != list[i]):
            temp = list[i]
            list[i] = list[index]
            list[index] = temp
            

n = int(input("Enter list size: "))
list = []
for i in  range(n):
    list.append(int(input("Enter element: ")))  # Convert input to integer

SelectionSort(list, n)
print(list)

