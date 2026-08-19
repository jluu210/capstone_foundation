from db import *
from print_services import *
from assessment_result_service import *
def rename_assessment(rs, db:Database):
    while True:
        currnt_name = rs[1]
        new_name = input(f'''Current Name: {currnt_name}
Press Enter to CANCEL 
Enter New Assessment Name: ''')
        if new_name == '':
            return
        else:
            conf = input(f'''Are you sure you want to change:
{currnt_name} to {new_name} ? [Y] to continue ''').strip().lower()
            if conf in ['y','yes']:
                db.update_assessment_name(rs[0],new_name)
            else:
                continue
def view_assessment_by_id(a_id,db:Database):
    rs = db.get_assessment_by_id(a_id)
    if rs is not None:
        print_assessment(rs)
        work_on_assessment_managment(rs,db)
        return True
    return False
def question_work_on_assessment(user:User,db):
    sel = input('Would you like to work on an Assessment? [Y] to continue: ').strip().lower()
    if sel in ['y','yes']:
        take_assessment_wf(user,db)
def work_on_assessment_managment(rs:list,db:Database):
    # 1. View all Assessment Results for {nm} .
    # 2. Rename {nm}
    while True:
        print_assessment_screen_manager(rs)
        sel = input('''
Selection: ''')
        if sel == '':
            return
        match sel:
            case '1':
                review_assessment_results_for_id(rs,db)
            case '2':
                rename_assessment(rs,db)
            case _:
                print('Invalid Selection.')
                continue
def view_assessments_a_user_still_needs(u_id,db:Database):
    rs = db.get_all_assessments_a_user_needs_to_take(u_id)
    print_table(rs,['Competency ID','Assessment ID','Competency','Assessment','Percentage'])
def assessment_wf_manager(c_id,db:Database):
    rs = db.get_assessment_by_compentency_id(c_id)
    print_table(rs,['Assessment ID','Name','Compentency'])
    while True:
        sel = input('''
Press ENTER to return

ID: ''')
        if sel == '':
            break
        if view_assessment_by_id(sel,db):
            continue
        else:
            print('Invalid selection')

def as_screen_assessment_wf_manager(db:Database):
    while True:
        view_all_assessments(db)
        sel = input('''
Press ENTER to return

ID: ''')
        if sel == '':
            break
        if view_assessment_by_id(sel,db):
            continue
        else:
            print('Invalid selection')
        
def view_all_assessments(db:Database):
    rws = db.get_all_assessments()
    print_table(rws,['ID','Name','Competency'])
def get_all_assesments_for_user(user:User, db:Database):
    print(f'''
ID: {user.user_id} Name: {user.f_name} {user.l_name}
''') 
    print_table(db.get_assements_for_user(user.user_id),['Assesment ID','Assesment Name','Assigned By','Score','Date Taken'])
    print()
def add_assessment_to_competency(c_id,db:Database):
     while True:
        compentency = db.get_compentency_by_id(c_id)
        val = input('''
Assessment Name: ''').strip()
        if val == '':
            return False
        sel = input(f'''

        Are you sure you want to add "{val}" to

        {compentency}

        [Y/N]: ''').strip().lower()
        if sel == 'y':
            db.add_new_assessment(c_id,val)
            return True
        else:
            continue
def take_assessment_wf(user:User, db:Database):
    u_id = user.user_id
    while True:
        print('Assessments taken')
        assessment_results_for_a_user(u_id,db)
        op = input('Would you like to take an Assessment? [Y] to continue').strip().lower()
        if op in ['yes','y']:
            print_table(db.get_all_assessments(),['ID','Assessment Name','Compentency'])
            sel = input("Enter Assessment ID: ")
            if sel == '':
                return
            if db.get_assessment_by_id(sel):
                create_assessment_result(u_id,sel,db)
            else:
                print('Invalid ID')
                continue
        return

# def delete_assessment_result(ar_id, db:Database):
#     rws = db.get_all_assessment_results_for_an_id(ar_id)
#     if rws:
#         sel = input('Are you sure you want to DELETE')
