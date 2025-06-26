def input_non_empty(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data
        else:
            print("Input cannot be empty. Please try again.")

def input_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit():
            return phone
        else:
            print("Phone number must be numeric. Please try again.")

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("===== All Contacts =====")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name : {contact.name}")
        print(f"   Phone : {contact.phone}")
        print(f"   Email : {contact.email}")
        print(f"   Address: {contact.address}")
        print("========================")

def search_contacts(contacts, term):
    results = []
    term_lower = term.lower()
    for contact in contacts:
        if (term_lower in contact.name.lower() or
            term_lower in contact.email.lower() or
            term_lower in contact.phone):
            results.append(contact)
    return results
