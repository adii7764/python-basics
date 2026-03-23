#Read and write files .Types of files
#1. Text files: .txt, .docx, .log, .csv,etc
#2. Binary files: .jpg, .png, .mp4, .exe, .mov, .etc
# Python uses the built-in open() function to work with files.
#Syntax: 
# file =open("File name","mode")
f=open("file.txt","r") #r for read mode
data=f.read()
print(data)
f.close()