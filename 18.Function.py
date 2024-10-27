# function definition
def Sum(a, b=2): #a ,b are parameter(param) |B with default argument if line 9
    return a + b

a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))

ans = Sum(a, b)
# ans = Sum(a)
print(ans)

# ````

def Print():
    print("Hello World")

Print()