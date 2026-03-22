# Write a program using functions to find greatest of three numbers. 
def greatest():
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    c=int(input("Enter number 3: "))
    if(a>b and a>c):
        print(a,"is the greatest")
    elif(b>a and b>c):
        print(b,"is the greatest")
    elif(c>a and c>b):
        print(c,"is the greatest")
    elif(a==b==c):
        print("All numbers are equal")
greatest()