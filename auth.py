from db import *
from user_service import *
def login_flow(db:Database):
    while True:
        print('Login Screen\n')
        email = input("Enter Email: ").strip()
        if email == '':
            return None
        password = input("Enter Password: ").strip()
        if password == '':
            return None
        user = db.login_user(email, password)
        if user is not None:
            print("Login Success")
            if user.user_type == 'manager':
                selection_flow(db,user)
            else:
                selection_flow(db,user)
        else:
            print("Login Unsuccessful!")
