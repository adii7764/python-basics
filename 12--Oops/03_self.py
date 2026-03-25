class Employee:#class is a blueprint of an object
    langugage="Python"
    salary=100000

    def getinfo(self):#self is a reference variable which will refer to the current object which is calling the method. 
        print(f"Language is {self.langugage} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

    
harry=Employee()#object of class employee
harry.langugage="Java"#object attribute will override class attribute
harry.getinfo()#object method will automatically pass the object reference as first argument to the method.
harry.greet()#static method will not pass the object reference as first argument to the method
