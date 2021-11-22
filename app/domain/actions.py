from app.models import Session, Contact
from sqlalchemy import and_


def add_contact(name, phone, owner):
    s = Session()
    contact = Contact(name=name, phone=phone, user_id=owner)
    s.add(contact)
    s.commit()


def get_contact(name, owner) -> (str, str):
    s = Session()
    print(owner)
    phone = s.query(Contact).filter(and_(Contact.name == name, Contact.user_id == owner)).first()
    if phone is not None:
        return phone.phone
    return None


def get_all_contacts(owner) -> []:
    s = Session()
    contacts = s.query(Contact).filter(Contact.user_id == owner).all()
    return contacts


def delete_contact(name, owner) -> bool:
    s = Session()
    result = s.query(Contact).filter(and_(Contact.name == name, Contact.user_id == owner)).delete()
    s.commit()
    if result != 0:
        return True
