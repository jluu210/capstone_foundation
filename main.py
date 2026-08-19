from db import *
from user import *
from auth import *
from print_services import *
from assessment_result import *
from competency_service import *
from assessment_result_service import *
from assessment_result import *
from user_service import *
from assessment_services import *
from reports import *
from import_csv import *

import sqlite3

def main():
    conn = sqlite3.connect("capstone.db")
    db = Database(conn)
    while True:
        login_flow(db)
        break

if __name__ == "__main__":
    main()