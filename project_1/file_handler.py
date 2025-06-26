import json

FILE_NAME = 'contacts.json'

def load_contacts():
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            return [data for data in data]
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)
      
