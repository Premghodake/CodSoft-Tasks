# Contact Book Application

# Dictionary to store contacts
contact_book = {}

def show_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("\nEnter the contact's name: ").strip()
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    address = input("Enter the address: ").strip()

    if name in contact_book:
        print("A contact with this name already exists.")
    else:
        contact_book[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contact_book:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact():
    query = input("\nEnter the name or phone number to search: ").strip()
    found = False

    for name, details in contact_book.items():
        if query.lower() in name.lower() or query == details['Phone']:
            print(f"\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break

    if not found:
        print("No contact found with the given information.")

def update_contact():
    name = input("\nEnter the name of the contact to update: ").strip()
    if name in contact_book:
        print(f"Updating contact '{name}':")
        phone = input("Enter the new phone number (leave blank to keep current): ").strip()
        email = input("Enter the new email (leave blank to keep current): ").strip()
        address = input("Enter the new address (leave blank to keep current): ").strip()

        if phone:
            contact_book[name]['Phone'] = phone
        if email:
            contact_book[name]['Email'] = email
        if address:
            contact_book[name]['Address'] = address

        print(f"Contact '{name}' updated successfully!")
    else:
        print("No contact found with that name.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("No contact found with that name.")

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
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
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
