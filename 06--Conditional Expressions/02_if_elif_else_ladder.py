age=int(input("Enter Age: "))

if(age>=18):
    print("Eligible for voting")
elif(age<=0):
    print("Invalid Age Is Entered")
else:
    print("Not Eligible for voting")