from print_services import *
from user_service import *
from user import *
from db import *
def reports_wf(logged_in_user:User,db:Database):
# 1. View User Competency Summary
# 2. View Competency Results Summary
# 3. Print Reports
    while True:
        print_report_screen()
        sel = input('Selection: ')
        match sel:
            case '':
                return
            case '1':
                veiw_user_competency_summary(logged_in_user,db)
            case '2':
                veiw_competency_result_summary(db)
            case '3':
                return
def veiw_user_competency_summary(logged_in_user,db:Database):
    while True:
        print('Choose a user to view competency summary')
        print_all_users_table(db)
        u_id = input('Enter User ID: ')
        if u_id == '':
            return
        user = db.load_user_by_id(u_id)
        print_a_user(user)
        print_table(db.get_user_competency_summary_for_user(u_id),['User','Competency','Assessment Name','Score','Date Taken'])
        input('Press ENTER to return')
def veiw_competency_result_summary(db:Database):
    while True:
        print('Choose a Compentency to view results summary')
        print_table(db.get_all_compentencies(),['ID','Name'])
        c_id = input('Enter Compentency ID: ')
        if c_id == '':
            return
        row = db.get_compentency_by_id(c_id)
        print_competency_by_id(row)
        print_table(db.get_competency_result_summary(c_id),['Competency','User','Assessment Name','Score','Date Taken'])
        input('Press ENTER to return')