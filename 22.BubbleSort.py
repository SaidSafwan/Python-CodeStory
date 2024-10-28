def BubbleSort(list, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if(list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            

n = int(input("Enter list size: "))
list = []
for i in  range(n):
    list.append(input())
    
BubbleSort(list, n)
print(list)