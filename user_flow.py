from print_services import *
from user import User
from db import *
def user_flow(user:User, db:Database):
    while True:
        print_selection_screen_user()
        user = db.load_user_by_id(user.user_id)
        # 1. View your information.
        # 2. Take an Assessment.
        # 3. View your previous Assessments.
        selection = input('Make a selection: ').strip().lower()
        if selection in ['q','quit']:
            return
        match selection:
            case '1':
                print_a_user(user)
                user_update_wf(user,db)
            case '2':
                pass
            case '3':
                pass
            case _:
                print('Invalid selection.')
def user_update_wf(user: User, db: Database):
    yes = input('''Would you like to keep update your info? [Y/N]

Press ENTER to return.''').strip().lower()

    if yes in ['y', 'yes']:
        fields = {
            "First Name": user.f_name,
            "Last Name": user.l_name,
            "Email": user.email,
            "Phone": user.phone
        }

        updated_fields = {}

        for label, value in fields.items():
            new_value = input(f'Current {label}: {value}\nEnter new {label} or press ENTER to keep it: ').strip()
            if new_value == '':
                updated_fields[label] = value
            else:
                updated_fields[label] = new_value

        yes = input('Would you like to keep these changes? [Y] to continue. ').strip().lower()
        if yes in ['y', 'yes']:
            new_fields = [
                updated_fields["First Name"],
                updated_fields["Last Name"],
                updated_fields["Email"],
                updated_fields["Phone"]
            ]
            if db.update_user_with_list(new_fields, user):
                print('Your data has been updated.')
        else:
            print('Cancelled.')

    



