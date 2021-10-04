import getpass
import csv

def login_user(func):
    def login():
        resp = input("Are you registered?(y|n): ")
        if resp == 'y':
            login = input("Input login: ")
            password = getpass.getpass("Input password: ")
            with open('users.csv') as users:
                csv_reader = csv.reader(users, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        print(row[0])
                        if row[1] == login and row[2] == password:
                            func()
                            break
                        line_count += 1
        elif resp == 'n':
            sign_up()
            login_user(func)
    return login


def sign_up():
    print("Sign Up!")
    name = input("Name: ")
    lastname = input("Last Name: ")
    email = input("Email: ")
    password = getpass.getpass("Password: ")
    confirmpassword = getpass.getpass("Confirm password: ")
    if password != confirmpassword:
        print("Password mismatch")
    with open('users.csv', mode='a') as usersfile:
        usersfile.write(str('\n' + str(1) + ',' + email + ',' + password))