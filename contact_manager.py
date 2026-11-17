# Initial sample contacts stored as a list of dictionaries
contact_list = [
    {"id": "4002", "name": "Moises", "activity": "Student", "phone": "21988465143"},
    {"id": "8922", "name": "Duda", "activity": "Student", "phone": "2196446681"}
]


# Function to register a new contact
def register_contact(contact_id):
    new_contact = {
        "id": contact_id,
        "name": input("Please enter the contact's name: ").strip(),
        "activity": input("Please enter the contact's activity/role: ").strip(),
        "phone": input("Please enter the contact's phone number: ").strip()
    }
    contact_list.append(new_contact.copy())
    print("Contact registered successfully!\n")


# Function to search and display contacts
def search_contacts():
    while True:
        option = input(
            "\nChoose the desired option:\n"
            "1. View all contacts\n"
            "2. Search by ID\n"
            "3. Search by activity/sector\n"
            "4. Return to main menu\n"
            "Option: "
        ).strip()

        if option == "1":
            if not contact_list:
                print("No contacts registered.\n")
            for contact in contact_list:
                print(f"ID: {contact['id']}")
                print(f"Name: {contact['name']}")
                print(f"Activity: {contact['activity']}")
                print(f"Phone: {contact['phone']}\n")

        elif option == "2":
            search_id = input("Please enter the contact's ID: ").strip()
            found = False
            for contact in contact_list:
                if contact["id"] == search_id:
                    print(f"ID: {contact['id']}")
                    print(f"Name: {contact['name']}")
                    print(f"Activity: {contact['activity']}")
                    print(f"Phone: {contact['phone']}\n")
                    found = True
                    break
            if not found:
                print("No contact found with this ID.\n")

        elif option == "3":
            search_activity = input("Please enter the contact's activity: ").strip().lower()
            found = False
            for contact in contact_list:
                if contact["activity"].lower() == search_activity:
                    print(f"ID: {contact['id']}")
                    print(f"Name: {contact['name']}")
                    print(f"Activity: {contact['activity']}")
                    print(f"Phone: {contact['phone']}\n")
                    found = True
            if not found:
                print("No contacts found for this activity.\n")

        elif option == "4":
            return
        else:
            print("Invalid option. Please try again.")


# Function to remove a contact by ID
def remove_contact():
    target_id = input("Please enter the ID of the contact to remove: ").strip()
    for i, contact in enumerate(contact_list):
        if contact["id"] == target_id:
            del contact_list[i]
            print("Contact removed successfully.\n")
            return
    print("No contact found with this ID.\n")


# Main menu loop
while True:
    print("\nWelcome to Maria Eduarda Gonçalves's Contact List!")
    print("Choose the desired option:")
    print("1. Register Contact\n2. Search Contact(s)\n3. Remove Contact\n4. Exit")
    menu_choice = input("Option: ").strip()

    if menu_choice == "1":
        register_contact(input("Contact ID: ").strip())
    elif menu_choice == "2":
        search_contacts()
    elif menu_choice == "3":
        remove_contact()
    elif menu_choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")