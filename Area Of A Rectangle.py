class Rectangle():
    def __init__ (self,l,w):
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length*self.width
new_rectangle = Rectangle(10,12)        
print("Dimension of a rectangle - Length : %d Width : %d %(new_rectangle.length,new_rectangle.width)")
print("Area of Rectangle :", new_rectangle.rectangle_area())

