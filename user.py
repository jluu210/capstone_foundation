from db import *
class User:
    def __init__(self, user_id, f_name, l_name, phone, email,
                 password_hash, creation_date, hire_date, user_type, active):
        self.user_id = user_id
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.email = email
        self.password_hash = password_hash
        self.creation_date = creation_date
        self.hire_date = hire_date
        self.user_type = user_type
        self.active = active
    def reload_user(self, u_id, db):
        if self.user_id == u_id:
            refreshed_user = db.load_user_by_id(u_id)
            self.user_id = refreshed_user.user_id
            self.f_name = refreshed_user.f_name
            self.l_name = refreshed_user.l_name
            self.phone = refreshed_user.phone
            self.email = refreshed_user.email
            self.password_hash = refreshed_user.password_hash
            self.creation_date = refreshed_user.creation_date
            self.hire_date = refreshed_user.hire_date
            self.user_type = refreshed_user.user_type
            self.active = refreshed_user.active
    def change_password():
        pass
    def take_assessment(self, competency_id):
        pass
class Manager(User):
    def print_reports():
        pass
    def view_users_in_compentency():
        pass
    