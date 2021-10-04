from models import Contact, Session


def menu():
    print("Select action:\n1. Get contact\n2. Add contact\n3. Delete contact\n")
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
        s = Session()
        contact = Contact(name=name, phone=phone, user_id=1)
        s.add(contact)

