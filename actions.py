from models import Session, Contact


def add_contact(name, phone):
    s = Session()
    contact = Contact(name=name, phone=phone, user_id=1)
    s.add(contact)
    s.commit()

