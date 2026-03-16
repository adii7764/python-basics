# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

subject1=float(input("Enter marks for subject 1: "))
subject2=float(input("Enter marks for subject 2: "))
subject3=float(input("Enter marks for subject 3: "))

#Check for percentage
total_percentage=(100)*(subject1+subject2+subject3)/300

if(total_percentage>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("Pass")
else:
    print("Fail")