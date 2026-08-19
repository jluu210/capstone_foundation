#import bcrypt
import sqlite3
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
    def change_password(self):
        stored_hash = (self.password_hash or "").encode('utf-8')
        while True:
            old_plain = input('Enter old password (blank to cancel): ')
            if old_plain == '':
                print("Password change cancelled.")
                return

            if bcrypt.checkpw(old_plain.encode('utf-8'), stored_hash):
                new_plain = input('Enter new password: ')
                re_plain = input('Re-enter new password: ')

                if new_plain != re_plain:
                    print("Passwords do not match!")
                    continue

                self.password_hash = bcrypt.hashpw(
                    new_plain.encode('utf-8'),
                    bcrypt.gensalt()
                ).decode('utf-8')
                self.save_user()
                print('Password Changed!')
                return
            else:
                print("Old password incorrect!")
    def save_user(self):
        connection = sqlite3.connect('capstone.db')
        cursor = connection.cursor()
        cursor.execute(
                    """
                    UPDATE Users
                    SET password_hash = ?
                    WHERE user_id = ?
                    """,
                    (self.password_hash, self.user_id)
                )
        connection.commit()
        return cursor.rowcount
class Manager(User):
    def print_reports():
        pass
    def view_users_in_compentency():
        pass
    