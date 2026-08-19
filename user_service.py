from db import *
from reports import *
from print_services import *
from user_service import *
from competency_service import *
from assessment_services import *
from user_flow import *
def determine_alpha(val:str):
    return val.isalpha()
def user_id_wf_manager(logged_in_user:User,db:Database):
    u_id = input('\nEnter a User ID to work on: ')
    work_on_user_obj(logged_in_user,db.load_user_by_id(u_id),db)
def edit_user(user:User, db:Database):
    f_name = input(f'Current Name {user.f_name} or ENTER to continue: ')
    if f_name == '':
       f_name = user.f_name
    l_name = input(f'Current Last Name {user.l_name} or ENTER to continue: ')
    if l_name == '':
        l_name = user.l_name
    phone = input(f'Current Phone {user.phone} or ENTER to continue: ')
    if phone == '':
        phone = user.phone
    email = input(f'Current Email {user.email} or ENTER to continue: ')
    if email == '':
        email = user.email
    db.update_user_data(user.user_id, f_name, l_name, phone, email)
    print('Edit Complete')
def management_user_selection_flow(user:User,db:Database):
    # 1. Edit
    # 2. View Assesments
    # 3. Deactivate user
    # 4. View Assessment Results for
    # 5. Delete Assessment Result
    while True:
        sel = input(f'''
    1. Edit {user.f_name}\'s Data
    2. View Assesments {user.f_name} still needs or retake.
    3. Deactivate {user.f_name}
    4. View Assessment Results for {user.f_name}
    5. Delete an Assessment Result for {user.f_name}

    Selection or ENTER to go back: ''').strip().lower()
        match sel:
            case '1':
                edit_user(user, db)
            case '2':
                view_assessments_a_user_still_needs(user.user_id,db)
                input('Press ENTER to go back.')
            case '3':
                db.deactivate_user_by_id(user.user_id)
                print(f'Deactivated: {user.f_name}')
                input('Press ENTER to go back.')
            case '4':
                view_all_assessment_results_for_user(user.user_id,db)
            case '5':
                delete_assessment_result_wf(user.user_id,db)
            case _:
                return

def user_selection_flow(user:User,db:Database):
    #1. Edit your information
    #2. Review your Assessments Still needed or to retake.
    #3. Take an Assesment
    #4. Change your password
    sel = input(f'''
    1. Edit your information
    2. Review your Assessments still needed or to retake.
    3. Take an Assesment
    4. Change your password
    Selection or ENTER to go back: ''').strip().lower()
    match sel:
        case '1':
            edit_user(user, db)
        case '2':
            view_assessments_a_user_still_needs(user.user_id,db)
            question_work_on_assessment(user,db)
        case '3':
            take_assessment_wf(user,db)
        case '4':
            user.change_password()
            input('Press ENTER to go back.')
            pass
        case _:
            return
def work_on_user_obj(logged_in_user:User,user:User, db:Database):
    if user is None:
        return
    print_a_user(user)
    if user.user_id == logged_in_user.user_id:
        user_selection_flow(logged_in_user,db)
    elif user.user_type == 'user' and logged_in_user.user_type == 'manager':
        management_user_selection_flow(user,db)
    else:
        input('Press ENTER to go back.')
def create_new_user(db:Database):
    fields = ['First Name', 'Last Name', 'Phone', 'Email','Password', 'Hire Date', 'Permission(m/u)']
    results=[]
    for k in fields:
        val = input(f'Enter {k}: ').strip()
        if val == '':
            break
        results.append(val)
    db.create_user(results)
def manager_flow(user:Manager, db:Database):
    while True:
        print_selection_screen_manager()
        selection = input('Make a selection: ').strip().lower()
        if selection in ['q','quit']:
            return
        logged_in_user = user
        #1. View your information.
        #2. View all Users
        #3. View Compentencies.
        #4. View All Assessments.
        #5. Search for User.
        #6. Create a new User
        #7. Reports.
        match selection:
            case '1':
                work_on_user_obj(logged_in_user,user,db)
            case '2':
                print_table(db.get_all_users(), ['ID','First Name','Last Name','Phone','Email','Hire Date', "Type", "Active"])
                user_id_wf_manager(logged_in_user,db)       
            case '3':
                compentency_work_flow(user,db)
            case '4':
                as_screen_assessment_wf_manager(db)
            case '5':
                rs = search_for_users(db)
                if rs is not None:
                    print_table(rs, ['ID','First Name','Last Name','Phone','Email','Hire Date', "Type", "Active"])
                    user_id_wf_manager(logged_in_user,db)
            case '6':
                create_new_user(db)
            case '7':
                reports_wf(db)
            case _:
                print('invalid selection')
def selection_flow(db:Database, user:User):
    while True:
            user_r = db.load_user_by_id(user.user_id)
            print_hello_screen(user_r)
            if(user_r.user_type == 'manager'):
                manager_flow(user_r,db)
            else:
                user_flow(user_r,db)
            break
def search_for_users(db:Database):
        name = input('Search: ')
        if(name == ''):
            return
        rows = db.search_users_by_name(name,name)
        if rows is not None:
            return rows
        else:
            print(f'no results for {name}')