f=open("file.txt")
# lines=f.readlines()
# print(lines)

line1=f.readline()#readline() reads one line at a time.
line2=f.readline()
print(line1)
print(line2)
f.close()