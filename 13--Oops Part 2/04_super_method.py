class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")
class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # Calling the constructor of the Employee class
        self.language = language

    def work(self):
        super().work()  # Calling the work method of the Employee class
        print(f"{self.name} is coding in {self.language}.")
p = Programmer("Alice", 70000, "Python")
p.work()
