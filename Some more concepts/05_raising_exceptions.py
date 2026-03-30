a=int(input("Hey Enter a number: "))
b=int(input("Hey Enter another number: "))
if b == 0:
    raise ValueError("Cannot divide by zero")#Raising a ValueError if b is zero
else:
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")