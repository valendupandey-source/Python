class Circle:
    def __init__(self,r,d,pi):
        self.radius = r
        self.diameter = d
        self.π = pi
    def Circlearea(self):
        return self.π * self.radius * self.radius    
    def Circleperrimeter(self):
        return self.π * self.diameter
new_circle = Circle(5,10,3.14159265358979323846)  
print("Diameter of Circle",5)
print("Area of Circle :", new_circle.Circlearea())

