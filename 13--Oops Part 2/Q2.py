# Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary

class Employee:
    def __init__(self, salary):
        self.salary = salary
        self._increment = 0

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if self.salary < 50000:
            self._increment = value * 0.1
        else:
            self._increment = value * 0.2

    def salaryAfterIncrement(self):
        return self.salary + self._increment
e = Employee(40000)
e.increment = 5000
print(f"Salary after increment: {e.salaryAfterIncrement()}")
