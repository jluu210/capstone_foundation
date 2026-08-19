from print_services import *
from user_service import *
from user import *
from db import *
import csv
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
                print_csv_wf(db)
            case _:
                print('Invalid input')
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
def print_csv_wf(db:Database):
    while True:
        # 1. Print User Competency Summary
        # 2. Print Competency Result Summary
        sel = input(display_print_selection_screen())
        match sel:
            case '1':
                select_user_competency_print(db)
            case '2':
                select_competency_print(db)
            case '':
                break
            case _:
                continue
def select_competency_print(db:Database):
    while True:
        print_table(db.get_all_compentencies(),['ID','Name'])
        sel = input(f''' 
Press ENTER to return.

Competency ID you wish to print: ''').strip()
        if sel == '':
            break
        elif sel.isdigit():
            if db.print_csv_competency_result_summary(sel):
                print('CSV printed')
            else:
                print(f'No reports found: {sel}')
        else:
            print('Invalid Input')
def select_user_competency_print(db:Database):
    while True:
        print_table(db.get_all_users(), ['ID','First Name','Last Name','Phone','Email','Hire Date', "Type", "Active"])
        sel = input(f''' 
Press ENTER to return.

User ID you wish to print: ''').strip()
        if sel == '':
            break
        elif sel.isdigit():
            if db.print_csv_user_competency_summary_for_user(sel):
                print('CSV printed')
            else:
                print(f'No reports found: {sel}')
        else:
            print('Invalid Input')

