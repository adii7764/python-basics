# Create a class “Programmer” for storing information of few programmers working at Microsoft. 
# The stored information should be name, age, and the programming language they use.
class Programmer:
    company="Microsoft"
    def __init__(self,name,age,languaage):
        self.name=name
        self.age=age
        self.language=languaage
Employee1=Programmer("Harry",25,"Java")
print(Employee1.name,Employee1.age,Employee1.language,Employee1.company)

Employee2=Programmer("Rohit",21,"JavaScript")
print(Employee2.name,Employee2.age,Employee2.language,Employee2.company)