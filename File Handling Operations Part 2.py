with open('Python/Sample.txt','w') as file:
  file.write("Channel Title: Don't die trying, try dying!")
file.close()
with open('Python/Sample.txt','w') as file:
    data = file.readlines()
    print("Words in this file are - ")
    for line in data:
        word = line.split()
        print(word)
file.close()     
import os
print("Checking if a file exists or not....")   
if os.path.exists("Python/Sample.txt"):
    os.remove("Sample.txt","w")
else:
    print("This file does not exist")
my_file = open('Python/my_file.txt','w') 
my_file.write(" Amongus ")
my_file.close()
os.remove('Python/Sample.txt')    
file.close() 