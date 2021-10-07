from models import Contact, Session
from actions import add_contact


def menu():
    print("Select action:\n1. Get contact\n2. Add contact\n3. Get all contacts\n4. Delete contact\n")
    action = input("Enter: ")
    if action == '1':
        s = Session()
        name = input("Contact name: ")
        phone = s.query(Contact).filter(Contact.name == name).first()
        if phone is not None:
            print('{}: {}'.format(name.capitalize(), phone.phone))
        else:
            print("No such contact")

    elif action == '2':
        name = input("Name of new contact: ")
        phone = input("Phone of new contact: ")
        add_contact(name, phone)

    elif action == '3':
        s = Session()
        phones = s.query(Contact).all()
        for i in range(len(phones)):
            print('{}: {} - {}'.format(i, phones[i].name.capitalize(), phones[i].phone))
