# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 
n = int(input("Enter the number of rows: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
