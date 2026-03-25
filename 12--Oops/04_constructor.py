class Employee:#class is a blueprint of an object
    langugage="Python"
    salary=100000
    def __init__(self,name,salary,language):#dunder use two underscores before and after the method name.
        self.name=name
        self.salary=salary
        self.language=language
        print("I am a constructor")

    def getinfo(self):#self is a reference variable which will refer to the current object which is calling the method. 
        print(f"Language is {self.langugage} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

    
harry=Employee("Harry",130000,"Python")#object of class employee
print(harry.name,harry.langugage,harry.salary)
harry.getinfo()
harry.greet()

