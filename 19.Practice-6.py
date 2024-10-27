# WAF to find the factorial of n. (n is the parameter)


# def factorial (n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial *= i 
#     return factorial


# n = int(input("Enter Number: "))
# print(factorial(n))

# using recursion
# def factorial (n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * factorial(n-1) 


# n = int(input("Enter Number: "))
# print(factorial(n))


# WAF to convert USD to INR.

def convert(usd_val):
    inr_value = usd_val * 83
    print(usd_val, "USD =", inr_value, "INR")

usd_val = int(input("Enter USD price: "))
convert(usd_val)
