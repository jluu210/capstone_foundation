from db import *
from assessment_result import *
from print_services import *
import random
def review_assessment_results_for_id(rs:list,db:Database):
    results = db.get_all_assessment_results_for_an_id(rs[0])
    for result in results:
        print(result)
def load_results_into_objects(rows:list): 
    results = [AssessmentResult.from_row(row) for row in rows]
    return results
    # for assesment in results:
    #     print(assesment)
def view_all_assessment_results_for_user(u_id, db:Database):
    print(f'User ID: ', u_id)
    print_table(db.get_all_assessment_results_for_user(u_id),['AR ID','Assessment Name','Score','Date Taken','Assigned By'])
def delete_assessment_result_wf(u_id,db:Database):
    while True:
        view_all_assessment_results_for_user(u_id,db)
        val = input('''Which Assessment Result would you like to DELETE?
Selection: ''').strip()
        if val == '':
            return False
        rws = db.get_assement_result_details(val)
        if rws:
            print_table(rws,['AR ID','Assessment Name','User ID','User Name','Score','Date Taken'])
            sel = input(f'''
            
Are you sure you want to DELETE "{val}, {rws[0][1]} for {rws[0][3]}"

    [Y/N]: ''').strip().lower()
            if sel == 'y':
                db.delete_assessment_result_byid(val)
                return True
            else:
                print('Cancelled')
                continue
def create_assessment_result(u_id,a_id,db:Database):
    while True:
        print_table(db.get_all_managers(),['ID','Name','Email'])
        m_id = input('Enter Manager ID: ')
        if db.get_manager_by_id(m_id):
            random_number = random.randint(0, 4)
            print('Your score is: ',random_number)
            db.add_new_assessment_result(u_id,a_id,m_id,random_number)
            print('New Assessment Result Created')
            return
        else:
            print('Invalid Manager ID')
            continue
def assessment_results_for_a_user(u_id,db:Database):
    rws = db.get_all_assessment_results_for_user(u_id)
    if rws:
        print_table(rws,['AR ID','Assessment Name','Score','Date Taken','Assigned By'])
    else:
        print('You have not taken an Assessment')
            
        
    

    