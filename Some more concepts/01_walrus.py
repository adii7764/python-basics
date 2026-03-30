#Using walrus opertor
if(n := len([1,2,3,4,5])) > 3:#Assigning the length of the list to n and checking if it's greater than 3
    print(f"List is too long with {n} elements")
#Using walrus operator in while loop
while (line := input("Enter a line (or 'exit' to quit): ")) != "exit":
    print(f"You entered: {line}")
