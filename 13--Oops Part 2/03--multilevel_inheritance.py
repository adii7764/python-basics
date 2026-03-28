class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
o=Employee()
p=Programmer()
m=Manager()
print(o.__dict__)#Empty dictionary as there are no attributes in Employee class
print(p.__dict__)#Empty dictionary as there are no attributes in Programmer class
print(m.__dict__)#Empty dictionary as there are no attributes in Manager class
print(p.b)#Accessing attribute b from Programmer class
print(m.b)#Accessing attribute b from Manager class through inheritance
print(m.c)#Accessing attribute c from Manager class