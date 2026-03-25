# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    @staticmethod
    def square(num):
        return num**2
    
    @staticmethod
    def cube(num):
        return num**3
    
    @staticmethod
    def square_root(num):
        return num**0.5
sqrt=Calculator.square_root(16)
print(sqrt)
sqr=Calculator.square(4)
print(sqr)
cb=Calculator.cube(3)
print(cb)