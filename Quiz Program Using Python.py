def q1():
    answer1 = input("What is the full form of the term 'BCE'? (Before Christ Era / Before Common Era ) :") 
    if answer1 == "Before Christ Era":
        print("Incorrect!")
        q2()
    elif answer1 == "Before Common Era":
        print("Correct!")
        q2()
    else: 
        print("Write the answer word to word as written in the boxes!") 
        q1()      
def q2():
    answer2 = input("How long did Buddha meditate before reaching enlightenment? (49 days / 35 days ) : ")
    if answer2 == "49 days":
        print("Correct")
        q3()
    elif answer2 == "35 days":
        print("Incorrect")
        q3() 
    else: 
        print("Write the answer word to word as written in the boxes!")
        q2()
def q3():
    answer3 = input("Who was the first Jain Tinthankara? ( Rishabhdev / Ajitanath ) : ")
    if answer3 ==  "Rishabhdev":
      print("Correct!")
      q4()
    elif answer3 == "Ajitanath":
        print("Incorrect!")
        q4()
    else: 
        print("Write the answer word to word as written in the boxes!")
        q3()
def q4():
    answer4 = input("Which Ved consists the knowledge of music? ( Atherwa Ved / Sam Ved ) : ")
    if answer4 == "Atherwa Ved":
        print("Incorrect!")
        final()
    elif answer4 == "Sam Ved":
        print("Correct!")
        final()
    else: 
        print("Write the answer word to word as written in the boxes!")
        q4()
def final():
    print("Congradulations!")       
    print("Thanks for playing,", name,"!")

####################################################
    

print("Hello user!, I am terminal!")
print("This is a MCQ Quiz in which there will be 2 options in each question")
print("Before we start, lets see who you are....")
name = input("What's your name? : ")
print("Hello ", name,"!")
print(" The topic is HISTORY!")
q1()
