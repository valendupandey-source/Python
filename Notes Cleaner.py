n = int(input(" How many charecters to preview? : "))
file = open("Python/class-notes.txt" , "r")
print(file.read(n))
file.close()
print()
file = open("Python/class-notes.txt" , "r")
lines = file.readlines()
file.close
print(" Total Lines : " , len(lines))
for i in range(len(lines)):
    print( i + 1, " -> ", lines[i].strip())
print()   
word = input(" Skip Lines Starting With : ") 
file = open("Python/class-notes.txt" , "r")
for line in file:
    if line.startswith(word):
        print(" Skip -> " , line.strip())
    else:
         print(" keep -> " , line.strip())
file.close()
print()
file = open("Python/class-notes.txt" , "r")
lines = file.readlines()
out = open("Python/odd-lines.txt" , "w")
for i in range (0, len(lines), 2):
    out.write(lines[i])
out.close()
print(" Odd lines saved to odd-lines.txt")






