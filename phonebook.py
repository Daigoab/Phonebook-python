phonebook = {}

def add_contact(name, number):
    if name in phonebook:
        print("Error: Contact already exists !!")
    else:
        phonebook[name] = number
        print("Contact added")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted")
    else: 
        print("Error: Contact not found")

def search_contact(name):
    if name in phonebook:
        print("Phone number: ", phonebook[name])
    else:
        print("Error: Contact not found")

def print_contact():
    if phonebook:
        print("Contacts:")
        for name, number in phonebook.items():
            print(name + ':', number)
    else:
        print("Phonebook is empty")

def main():
    while True:
        print("Choose an option:")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Search for a contact")
        print("4. Print all contacts")
        print("5. Quit Phonebook")

        choice = input("> ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            add_contact(name, number)

        elif choice == "2":
            name = input("Enter contact name: ")
            delete_contact(name)

        elif choice == "3":
            name = input("Enter contact name: ")
            search_contact(name)

        elif choice == "4":
            print_contact()

        elif choice == "5":
            print("Phonebook closed !!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
