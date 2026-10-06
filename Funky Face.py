from turtle import *
class Face:
    def __init__(self,xpos,ypos):
        self.size = 90
        self.coord = (xpos,ypos)
        self.noseSize = "small"
    def setSize(self,radius):
        self.size = radius  
    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)     
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)
    def goHome(self):
        penup()
        goto(self.coord)
        setheading()
    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.goHome()
    def drawEye(self,turn):
        penup()
        left(turn)
        forward(self.size/2)
        dot(self.size/10)
        self.goHome()
    def drawaMouth(self):
        if self.noseSize == 'large':
            dot(self.size/2, "grey")
        




    

              


        

