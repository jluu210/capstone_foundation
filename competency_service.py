from db import *
from user  import *
from print_services import *  
from assessment_services import *
def update_competency_(c_id,db:Database):
    data = input('Enter new name: ')
    if data == '':
        print('Cancelled!')
        return
    db.update_competency_by_id(c_id,data)
def competency_detail_wf(c_id, db:Database):
    while True:
        sel = input('''
    1. Edit Competency.
    2. Delete Competency
    3. Add an Assessment to Competency
    4. View Assessments for Competency
    Press ENTER to return.

    Selection: ''')
        match sel:
            case '1':
                update_competency_(c_id,db)
            case '2':
                val = input(
                    f'''
Are you sure you want to DELETE: 
    {db.get_compentency_by_id(c_id)}
[Y/N]: ''')
                if val == 'y':
                    db.delete_competency_cascade(c_id)
                else:
                    print('Cancelled.')
            case '3':
                if add_assessment_to_competency(c_id,db):
                    print('Assessment Added')
                else:
                    print('Cancelled.')
            case '4':
                assessment_wf_manager(c_id,db)
            case '':
                return
            case _:
                print(f'Invalid Choice: {sel}')
                continue
def view_competency_by_id(db:Database):
     while True:
        print_table(db.get_all_compentencies(),['ID','Name'])
        val  = input('''

Press ENTER to return

ID: ''').strip()
        if val == '':
            break
        if val.isalpha():
            print(f'invalid ID: {val}')
            continue
        data = db.get_compentency_by_id(val)
        if data:
            print_competency_by_id(data)
            competency_detail_wf(val,db)
        else:
            print(f'ID {val} not found or invalid')
def mg_create_competency(db:Database):
    name = input('Competency name or ENTER to return: ').strip()
    if name == '':
        return
    else:
        db.create_new_competency(name.title())
def manager_compentency_wf(db:Database):
    view_competency_by_id(db)
def compentency_work_flow(user:User,db:Database):
    if user.user_type == 'manager':
        manager_compentency_wf(db)
        