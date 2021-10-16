from models import Contact, Session
from actions import add_contact, get_contact, get_all_contacts, delete_contact


def menu(user_id: int):
    print("Select action:\n1. Get contact\n2. Add contact\n3. Get all contacts\n4. Delete contact\n")
    action = input("Enter: ")
    if action == '1':  # Get contact
        name = input("Contact name: ")
        phone = get_contact(name, 'root')
        if phone is not None:
            print('{}: {}'.format(name.capitalize(), phone))
        else:
            print("No such contact")

    elif action == '2':  # Add contact
        name = input("Name of new contact: ")
        phone = input("Phone of new contact: ")
        add_contact(name.capitalize(), phone, 1)

    elif action == '3':  # Get all contacts
        s = Session()
        phones = s.query(Contact).all()
        for i in range(len(phones)):
            print('{}: {} - {}'.format(i, phones[i].name.capitalize(), phones[i].phone))

    elif action == '4':  # Delete contact
        s = Session()
        name = input("Name of contact: ")
        result = s.query(Contact).filter(Contact.name == name).delete()
        if result != 0:
            print("Contact {} was deleted".format(name.capitalize()))
