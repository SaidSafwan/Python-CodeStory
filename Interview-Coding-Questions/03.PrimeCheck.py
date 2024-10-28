# def is_prime(number):
#     if(number < 2):
#         return False
#     for i in range(number-1, 1, -1):
#         if(number%i == 0):
#             return False
#     return True

# Optimized approach
def is_prime(number):
    if(number < 2):
        return False
    for i in range(2, int(number**0.5)+1):
        print(f"current value {i}")
        if(number%i == 0):
            return False
    return True


# Test the function
num = int(input("Enter Number: "))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



# NOTE:
# number**0.5: This calculates the square root of number.
# int(...): This converts the square root to an integer, effectively rounding down. For example:
# If number is 17, then number**0.5 is approximately 4.12, and int(4.12) becomes 4.
# If number is 16, then number**0.5 is 4.0, and int(4.0) becomes 4.
# + 1: This is added to include the upper limit in the range because range in Python is exclusive of the stop value. So for number = 17, it checks divisors 2 through 4 (inclusive of 2 and 4).

# The reason for adding 1 to int(number**0.5) in the range is to ensure that the upper limit of the loop includes the integer value of the square root.