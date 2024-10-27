# WAP to find the sum of first n numbers. (using while)

n = int(input("Enter Number:"))
sum = 0
for i in range(n+1):
    sum += i

print(sum)


# WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter Number:"))
factorial = 1
for i in range(1,n+1):
    factorial *= i

print(factorial)
