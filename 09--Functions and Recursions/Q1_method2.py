#Using max() function to find the greatest of three numbers
def greatest():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))

    max_num = max(a, b, c)

    if a == b == c:
        print("All numbers are equal")
    else:
        print(max_num, "is the greatest")

greatest()