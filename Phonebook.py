import sys
def create_phonebook():
    n = int(input(" Enter Number Of Contacts : "))
    pb = []
    for i in range(n):
        print(f"\nEnter details for contact { i + 1 }")
        name = input(" Name : ").strip()
        if not name:
            print("Name is reqired!")
            sys.exit
        number = input(" Phone Number : ")    
        email = input(" Email : ")
        dob = input(" DOB : ")
        category = input(" Category (Family, Friend, Work, Personal, HT ) : ")
        pb.append([name, number, email, dob, category])
        return pb
def display_contacts(pb):
    if not pb:
        print("\nPhonebook is empty!")
        return
    print("\n--- CONTACT LIST ---")    
    print(" {:<15 } {:<15} {:<25} {:<15} {:<10}".format (contact[0], contact[1], contact[2], contact[3], contact[4]))   


