from db import *
from user_service import *
def login_flow(db:Database):
    while True:  
        email = input(display_login_screen()).strip()
        if email == '':
            return None
        password = input("Enter Password: ").strip()
        if password == '':
            return None
        user = db.login_user(email, password)
        if user is not None:
            print("Login Success")
            selection_flow(db,user)
        else:
            print("Login Unsuccessful!")
