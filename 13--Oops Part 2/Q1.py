#  Create a class (2-D vector) and use it to create another class representing a 3-D vector. 
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"The 2D vector is ({self.x}, {self.y})")

class Vector3D(Vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y) #Calling the constructor of the Vector2D class to initialize x and y
        self.z=z
    def show(self):
        print(f"The 3D vector is ({self.x}, {self.y}, {self.z})")
v=Vector3D(1,2,3)
v.show()