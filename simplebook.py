# simple book mini project



print("Welcome to the Book mini project")



contacts = {}

def show_menu():
     print("\n1. Add Contact")
     print("2. View Contacts")
     print("3. Search Contact")
     print("4. Exit")


def contact_book():
    while True:
         show_menu()
         choice = input("Enter your choice (1/2/3/4):")

         if choice == "1":
           name =  input("Enter Name:  ")
           number = input("Enter Number: ")
           contacts[name] = number
           print("contact book added")
         elif choice == "2":
             print("All contacts")
             for name, number in contacts.items():
                 print(f"{name}: {number}")
         elif choice == "3":
             search_name = input("Enter name to search")
             if search_name in contacts:
                 print(f"{search_name}: {contacts[search_name]}")
             else: 
                 print("contact not found")

         elif choice == "4":
            print("good bye")
            break
         else:
             print("Invalid choice try again.")

contact_book()
       
