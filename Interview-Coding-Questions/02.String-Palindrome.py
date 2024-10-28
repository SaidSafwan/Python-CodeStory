# Question: Write a Python program to check if a string is a palindrome.

def is_Palindrome(str):
    reverse_str = str[::-1]
    # if(str == reverse_str):
    #     return True
    # else:
    #     return False
    # OR
    return str == reverse_str



str = input("Enter Input String: ")
if is_Palindrome(str):
    print(str,"is Palindrome")
else:
    print(str,"Not Palindrome")
    