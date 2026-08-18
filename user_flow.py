from print_services import *
def user_flow(user:User):
    while True:
        print_selection_screen_user()
        # 1. View your information.
        # 2. Take an Assessment.
        # 3. View your previous Assessments.
        selection = input('Make a selection: ').strip().lower()
        if selection in ['q','quit']:
            return
        print(f'USER FLOW: {user.f_name}')