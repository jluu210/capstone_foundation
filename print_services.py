from user import *
def print_hello_screen(user:User):
    print(f'''
    Hi {user.f_name}!
    ====================================
        What would you like to do today?''')
def print_all_users_table(db):
    print_table(db.get_all_users(), ['ID','First Name','Last Name','Phone','Email','Hire Date', "Type", "Active"])
def print_assessment(result:list):
    print(f'''
ID: {result[0]}
Name: {result[1]}
Competency: {result[2]}
''')
def print_objects_table(results):
    # results can be: [] (zero objects) or a list of AssessmentResult objects (or similar)
    if not results:
        print("No results.")
        return

    headers = ["ID", "User ID", "Assessment ID", "Date Taken", "Manager ID", "Score"]

    # Build rows
    rows = []
    for r in results:
        rows.append([
            str(getattr(r, "result_id", "")),
            str(getattr(r, "user_id", "")),
            str(getattr(r, "assessment_id", "")),
            str(getattr(r, "date_taken", "")),
            str(getattr(r, "manager_id", "")),
            str(getattr(r, "score", "")),
        ])

    # Compute column widths
    widths = []
    for i in range(len(headers)):
        w = len(headers[i])
        for row in rows:
            if len(row[i]) > w:
                w = len(row[i])
        widths.append(w)

    # Print header
    header_line = " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))
    sep_line = "-+-".join("-" * widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep_line)

    # Print rows
    for row in rows:
        line = " | ".join(row[i].ljust(widths[i]) for i in range(len(headers)))
        print(line)

def print_competency_by_id(rows:list):
    if rows is None:
        return
    print(f'''
Competency info:
--------------------------- 
ID: {rows[0]}
Name: {rows[1]}
DATE ADDED: {rows[2]}
---------------------------''')
    
def print_table(rows, headers:list):
    if not rows:
        print("No results.")
        return
    
    widths = {h: len(h) for h in headers}
    for row in rows:
        for i, h in enumerate(headers):
            value = "" if row[i] is None else str(row[i])
            widths[h] = max(widths[h], len(value))

    print(" | ".join(h.ljust(widths[h]) for h in headers))
    print("-+-".join("-" * widths[h] for h in headers))

    for row in rows:
        print(" | ".join(
            ("" if row[i] is None else str(row[i])).ljust(widths[h])
            for i, h in enumerate(headers)
        ))

def print_selection_screen_manager():
    print('''
Selection:
    1. View your information.
    2. View all Users
    3. View Compentencies.
    4. View all Assessments.
    5. Search for User.
    6. Create a new User.
    7. Reports.
    8. Import an Assessment Results CSV
    [Q]uit
''')
    
def print_selection_screen_user():
    print('''
Selection:
    1. View your information.
    2. View your previous assessments and take an Assessment.
    3. View Assessments you still need to do.
    4. Change your password.
    [Q]uit
''')
    
def print_a_user(user:User):
    print(f'''
    ID {user.user_id}
    Name {user.f_name} {user.l_name}
    Phone: {user.phone} Email: {user.email}
    Hired: {user.hire_date}
    Permission: {user.user_type}''')

def print_assessment_screen_manager(assessment:list):
    nm = assessment[1]
    print(
f'''1. View all Assessment Results for: {nm} 
2. Rename: {nm}''')

def print_report_screen():
    print('''
1. View User Competency Summary
2. View Competency Results Summary
3. Print Reports

Press ENTER to return.
''')

def display_print_selection_screen():
    s = '''
1. Print User Competency Summary
2. Print Competency Result Summary

Press Enter to go back
'''
    return s

def display_login_screen():
    s ='''
WELCOME
TO
Competency Tracking Tool Overview 

To LOGIN

Enter Email: '''
    return s


        
