from models import Session, Contact


def add_contact(name, phone, owner):
    s = Session()
    contact = Contact(name=name, phone=phone, user_id=owner)
    s.add(contact)
    s.commit()


def get_contact(name, owner) -> (str, str):
    s = Session()
    phone = s.query(Contact).filter(Contact.name == name).first()
    if phone is not None:
        return phone.phone
    return None


def get_all_contacts(owner) -> []:
    s = Session()
    phones = s.query(Contact).filter(Contact.user_id == owner).all()
    return phones


def delete_contact(name, owner) -> bool:
    s = Session()
    result = s.query(Contact).filter(Contact.name == name).delete()
    if result != 0:
        return True
