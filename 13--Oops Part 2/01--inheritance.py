class Employee:
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):#Programmer class inherits from Employee class
    def show(self):
        print(f"The name of the programmer is {self.name} and the salary is {self.salary}")
        print(f"The programming language is {self.language}")

a=Employee()#Creating an instance of the Employee class
b=Programmer()#Creating an instance of the Programmer class
a.name="John"
a.salary=50000
print("Employee details:")
a.show()
b.name="Alice"
b.salary=70000
b.language="Python"
print("\nProgrammer details:")
b.show()