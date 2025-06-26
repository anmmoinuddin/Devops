from contacts import Contact
import file_handler
import utils

def add_contact(contacts):
    name = utils.input_non_empty("Enter Name: ")
    phone = utils.input_phone("Enter Phone Number: ")

    # Check for duplicate phone number
    for c in contacts:
        if c.phone == phone:
            print("Error: Phone number already exists for another contact.")
            return

    email = utils.input_non_empty("Enter Email: ")
    address = utils.input_non_empty("Enter Address: ")

    new_contact = Contact(name, phone, email, address)
    contacts.append(new_contact)
    file_handler.save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    utils.display_contacts(contacts)

def search_contact(contacts):
    term = utils.input_non_empty("Enter search term (name/email/phone): ")
    results = utils.search_contacts(contacts, term)
    if results:
        print("Search Result:")
        utils.display_contacts(results)
    else:
        print("No matching contacts found.")

def remove_contact(contacts):
    phone = utils.input_phone("Enter the phone number of the contact to delete: ")
    for c in contacts:
        if c.phone == phone:
            confirm = input(f"Are you sure you want to delete contact with number {phone}? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(c)
                file_handler.save_contacts(contacts)
                print("Contact deleted successfully!")
            else:
                print("Deletion canceled.")
            return
    print("Contact with that phone number not found.")

def main():
    print("Welcome to the Contact Book CLI System!\n")
    contacts_data = file_handler.load_contacts()
    contacts = [Contact.from_dict(c) for c in contacts_data]
    print("Loading contacts from contacts.json... Done!\n")

    while True:
        print("=========== MENU ===========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("============================")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            remove_contact(contacts)
        elif choice == '5':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
