import getpass
from models import Session, User
from sqlalchemy import and_




def login_user(func):
    def login():
        resp = input("Are you registered?(y|n): ")
        if resp == 'y':
            username = input("Input login: ")
            password = getpass.getpass("Input password: ")
            s = Session()
            id = s.query(User).filter(and_(User.username == username, User.password == password)).first()
            if id is None:
                print("No such user :(")
                resp = input("Register?(y|n) ")
                if resp == 'y':
                    sign_up()
                else:
                    exit(0)

        elif resp == 'n':
            sign_up()
            login_user(func)



def sign_up():
    print("Sign Up!")
    name = input("Name: ")
    lastname = input("Last Name: ")
    email = input("Email: ")
    password = getpass.getpass("Password: ")
    confirmpassword = getpass.getpass("Confirm password: ")
    if password != confirmpassword:
        print("Password mismatch")
