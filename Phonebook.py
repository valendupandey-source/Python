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
def add_c(pb):
    print("\nEnter new contact detals")
    name = input(" Name : ")
    number = input(" Phone Number : ")
    email = input(" Email : ")
    dob = input(" DOB : ")
    category = input(" Category : ")
    pb.append([name, number, email, dob, category])
    print("Contact added successfully!")
def search_contact(pb):
    name = input(" \nEnter name to search : ")    
    found = False
    for  contact in pb:
        if contact[0].lower() == name.lower():
            print("\nContact Found : ")
            print("Name : " , contact[0])
            print("Phone : " , contact[1])
            print("Email : " , contact[2])
            print("DOB : " , contact[3])
            print("Category : " , contact[4])
            found = True
            break
        if not found:
            print("Contact not found") 
def remove_contact(pb):
    name = input("\nEnter contact to remove : ")  
    for contact in pb:
        if contact[0].lower() == name_lower():
            pb.remove(contact)     
            print("Contact removed successfully!") 
            return
    print(" Contact not found! ")          








