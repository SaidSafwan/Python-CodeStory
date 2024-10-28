# Question : Write a Python program to reverse a string.

def ReverseString(str):

    return str[::-1]


word = input("Enter Input String: ")
reversed_word = ReverseString(word)
print(reversed_word)