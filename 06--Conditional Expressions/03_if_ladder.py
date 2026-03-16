age=int(input("Enter Age: "))
# IF statement no:1
if(age%2==0):
    print("Age is Even")
#End of IF statement no:1


# IF statement no:2
if(age>=18):
    print("Eligible for voting")
elif(age<=0):
    print("Invalid Age Is Entered")
else:
    print("Not Eligible for voting")
#End of IF statement no:2