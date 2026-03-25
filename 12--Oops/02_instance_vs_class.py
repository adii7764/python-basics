class Employee:#class is a blueprint of an object
    
    langugage="Python"
    salary=100000

harry=Employee()#object of class employee
harry.langugage="Java"#object attribute will override class attribute
print(harry.langugage,harry.salary)