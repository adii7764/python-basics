class Emplpyee:
    a=1

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")
e=Emplpyee()
e.a=2
e.show()#Calling the class method using the instance