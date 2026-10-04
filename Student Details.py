class CSStudent:
    stream = 'cse'
    def __init__(self,roll):
        self.roll = roll
    def setAdress(self,adress):   
        self.adress = adress
    def getadress(self):
        return self.adress  
add = CSStudent(101)       
add.setAdress("Pune, Maharastra")
print(add.getadress())
a = CSStudent(101)
b = CSStudent(102)
print(a.stream)
print(b.stream)
print(a.roll)
print(CSStudent.stream)
