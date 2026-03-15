#  Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''

print(letter.replace("<|Name|>","XYZ").replace("<|Date|>","24 sept 2000"))
