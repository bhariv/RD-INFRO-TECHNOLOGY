contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")


    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")

    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact["name"] == query or contact["phone"] == query:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
        if not found:
            print("Contact not found.")

def update_contact():
    name =  input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"] == name:
            print("Leave field blank to keep current value.")
            new_phone = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
            new_email = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            new_address = input(f"Enter new address(current: {contact['address']}") or contact['address']

            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address

            print("Contact updated successfully.\n")
            return
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete:")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("contact deleted successfully.\n")
            return
        print("Contact not found.\n")

def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice ==  "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. please try again.\n")


if __name__ == "__main__":
    main()
        
        
    
            
            
            
        
            
        




