import json

class ContactManager:
    def __init__(self, filename='gptcontacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        if not any(contact['email'] == email for contact in self.contacts):
            self.contacts.append({"name": name, "phone": phone, "email": email})
            self.save_contacts()
            print("Contact added successfully.")
        else:
            print("A contact with this email already exists.")

    def find_contact(self, name):
        return next((contact for contact in self.contacts if contact["name"] == name), None)

    def update_contact(self, name, **updates):
        contact = self.find_contact(name)
        if contact:
            contact.update(updates)
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

def main():
    manager = ContactManager()
    actions = {
        'add': lambda: manager.add_contact(
            input("Enter name: "), input("Enter phone: "), input("Enter email: ")
        ),
        'update': lambda: manager.update_contact(
            input("Enter the name of the contact to update: "), **{
                input("Enter the field to update (name/phone/email): "): input("Enter the new value: ")
            }
        ),
        'delete': lambda: manager.delete_contact(input("Enter the name of the contact to delete: ")),
        'display': manager.display_contacts,
    }

    while True:
        action = input("Choose an action (add, update, delete, display, quit): ").lower()
        if action == 'quit':
            break
        elif action in actions:
            actions[action]()
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
