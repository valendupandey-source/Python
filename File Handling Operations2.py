new_file = open('Python/New_File12.txt', 'x')
new_file.close()
import os
print(" Checking if my_file exists or not.....")
if os.path.exists("/Pythonmy_file.txt"):
    os.remove("Python/my_file.txt")
else:
    print(" This file does not exist ")    
my_file = open('Python/my_file.txt','w') 
my_file.write(" Hi! I am Valendu Pandey and I am 11 years old.")
my_file.close()
os.remove('Python/Codingal.txt')   
