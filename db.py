import sqlite3
from datetime import datetime
from user import *
class Database:
    def __init__(self, conn):
        self.conn = conn
    def login_user(self, email, password):
        user = self.load_user_by_email(email)
        if user is None:
            return None
        if user.active != 1:
            return None
        if user.password_hash == password:
            return user
        return None   
    def load_user_by_email(self, email):
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT
                user_id, f_name, l_name, phone, email, password_hash,
                creation_date, hire_date, user_type, active
            FROM Users
            WHERE email = ?
            """,
            (email,)
        )
        row = cur.fetchone()
        if row is None:
            return None
        if row[8] == 'manager':
            return Manager(
                user_id=row[0],
                f_name=row[1],
                l_name=row[2],
                phone=row[3],
                email=row[4],
                password_hash=row[5],
                creation_date=row[6],
                hire_date=row[7],
                user_type=row[8],
                active=row[9])
        return User(
            user_id=row[0],
            f_name=row[1],
            l_name=row[2],
            phone=row[3],
            email=row[4],
            password_hash=row[5],
            creation_date=row[6],
            hire_date=row[7],
            user_type=row[8],
            active=row[9])
    def search_users_by_name(self, first_name: str, last_name: str):
        cur = self.conn.cursor()
        like_term = f"%{first_name}%"
        cur.execute(
            '''
            SELECT user_id, f_name, l_name, phone, email, hire_date, user_type, active
            FROM Users
            WHERE (? = '' OR f_name LIKE ?)
              OR (? = '' OR l_name LIKE ?)
            ORDER BY l_name, f_name
            ''',
            (like_term, like_term, like_term, like_term)
        )
        rows = cur.fetchall()
        if rows == []:
            return None
        else:
            return rows
    def get_all_users(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT
                user_id, f_name, l_name, phone, email, hire_date, user_type, active
            FROM Users
            """)
        rows = cur.fetchall()
        if rows == []:
            return None
        else:
            return rows
    def get_assessment_by_id(self, a_id):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT 
        a.assessment_id,
        a.name AS assessment_name,
        c.name AS competency
        FROM Assessments a
        JOIN Competencies c
        ON c.competency_id = a.competency_id
        WHERE assessment_id = ?
        ''',(a_id,))
        row = cur.fetchone()
        if row is None:
            return None
        else:
            return row
    def get_all_assessment_results_for_an_id(self,ar_id):
        cur = self.conn.cursor()
        cur.execute('''SELECT
        ar.result_id,
        ar.user_id,
        GROUP_CONCAT(u.f_name || ' ' || u.l_name, ', ') AS assigned_to,
        ar.score,
        ar.date_taken
        FROM Assessment_Results ar
        JOIN Users u
        ON u.user_id = ar.user_id
        WHERE ar.assessment_id = ?
        ORDER BY ar.date_taken DESC, ar.result_id;''',(ar_id,))
        rows = cur.fetchall()
        if rows is None:
            return None
        else:
            return rows
    def get_assement_result_details(self,ar_id):
        cur = self.conn.cursor()
        cur.execute('''
            SELECT
                ar.result_id,
                a.name AS assessment_name,
                ar.user_id,
                (u.f_name || ' ' || u.l_name) AS taken_by_name,
                ar.score,
                ar.date_taken
            FROM Assessment_Results ar
            JOIN Assessments a
                ON a.assessment_id = ar.assessment_id
            JOIN Users u
                ON u.user_id = ar.user_id
            WHERE ar.result_id = ?
            ORDER BY ar.date_taken DESC, ar.result_id;
        ''', (ar_id,))
        rows = cur.fetchall()
        return rows if rows else None

    def get_all_assessment_results_for_user(self, u_id):
        cur = self.conn.cursor()
        cur.execute('''
            SELECT
                ar.result_id,
                a.name AS assessment_name,
                ar.score,
                ar.date_taken,
                COALESCE(m.f_name || ' ' || m.l_name, 'N/A') AS manager_name
            FROM Assessment_Results ar
            JOIN Assessments a
                ON a.assessment_id = ar.assessment_id
            LEFT JOIN Users m
                ON m.user_id = ar.manager_id
            WHERE ar.user_id = ?
            ORDER BY ar.date_taken DESC, ar.result_id;
        ''', (u_id,))
        rows = cur.fetchall()
        return rows if rows else None
    
    def get_all_assessments_a_user_needs_to_take(self, u_id):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT
            
            c.competency_id,
            a.assessment_id,
            c.name AS competency_name,
            a.name AS assessment_name,
            COALESCE(ar_stats.avg_score_pct, 0) AS avg_score_pct
        FROM Assessments a
        JOIN Competencies c
        ON c.competency_id = a.competency_id
        LEFT JOIN (
            SELECT
                ar.assessment_id,
                AVG(ar.score) * 100.0 / 4.0 AS avg_score_pct
            FROM Assessment_Results ar
            WHERE ar.user_id = ?
            GROUP BY ar.assessment_id
        ) AS ar_stats
        ON ar_stats.assessment_id = a.assessment_id
        WHERE
            ar_stats.avg_score_pct IS NULL
            OR ar_stats.avg_score_pct < 70
        ORDER BY c.name, a.name;
        ''', (u_id,))
        rows = cur.fetchall()
        return rows if rows else None

    def get_all_assessments(self):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT 
        a.assessment_id,
        a.name AS assessment_name,
        c.name AS competency
        FROM Assessments a
        JOIN Competencies c
        ON c.competency_id = a.competency_id
        ''',)
        rows = cur.fetchall()
        if rows is None:
            return None
        else:
            return rows
    def get_assessment_by_compentency_id(self,c_id):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT 
        a.assessment_id,
        a.name AS assessment_name,
        c.name AS Compentency
        FROM Assessments a
        JOIN Competencies c
        ON c.competency_id = a.competency_id
        WHERE c.competency_id = ?
        ''',(c_id,))
        rows = cur.fetchall()
        if rows is None:
            return None
        else:
            return rows

    def fetch_assessment_results_by_id(self,u_id):
        cur = self.conn.cursor()
        # returns a simplfied version of the assesment_result
        cur.execute("""
            SELECT result_id, user_id, assessment_id, date_taken, manager_id, score
            FROM Assessment_Results
            WHERE user_id = ?
            ORDER BY date_taken DESC
        """, (u_id,))
        rows = cur.fetchall()
        if rows is None:
            return None
        else:
            return rows

    def fetch_assessments_with_assigned_users(self):
        cur = self.conn.cursor()
        # SQLite GROUP_CONCAT to list users per assessment
        cur.execute("""
        SELECT
            a.assessment_id,
            a.name AS assessment_name,
            c.name AS competency_name,
            GROUP_CONCAT(u.f_name || ' ' || u.l_name, ', ') AS assigned_to
        FROM Assessments a
        JOIN Competencies c
        ON c.competency_id = a.competency_id
        LEFT JOIN Assessment_Results r
        ON r.assessment_id = a.assessment_id
        LEFT JOIN Users u
        ON u.user_id = r.user_id
        GROUP BY a.assessment_id, a.name, c.name
        ORDER BY c.name, a.name;
        """)
        rows = cur.fetchall()
        if rows is None:
            return None
        else:
            return rows
    def change_user_password(self, user:User):
        pass

    def add_new_assessment(self, competency_id, assessment_name):
        cur = self.conn.cursor()
        cur.execute("SELECT competency_id FROM Competencies WHERE competency_id = ?", (competency_id,))
        if cur.fetchone() is None:
            raise ValueError(f"Competency ID {competency_id} does not exist")

        cur.execute(
            "INSERT INTO Assessments (competency_id, name) VALUES (?, ?)",
            (int(competency_id), assessment_name.strip())
        )
        self.conn.commit()
        return cur.lastrowid
    
    def create_user(self, f_data: list):
        f_name = f_data[0]
        l_name = f_data[1]
        phone = f_data[2]
        email = f_data[3]
        password_hash = f_data[4]
        hire_date = f_data[5]
        if f_data[6] == 'm':
            user_type = 'manager'
        else:
            user_type = 'user'
        active = 1
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO Users
                    (f_name, l_name, phone, email, password_hash, hire_date, user_type, active)
                VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (f_name, l_name, phone, email, password_hash, hire_date, user_type, active)
            )
            try:
                self.conn.commit()
            except Exception as e:
                print(f"SQLite error during commit: {type(e).__name__}: {e}")
                self.conn.rollback()
                raise
            return cur.lastrowid
        except Exception as e:
            print(f"SQLite error during insert: {type(e).__name__}: {e}")
            self.conn.rollback()
            raise
    def update_competency_by_id(self,c_id,data):
        cur = self.conn.cursor()
        cur.execute('''UPDATE Competencies SET name = ? WHERE competency_id = ?''',(data,c_id))
        self.conn.commit()
        return cur.rowcount

    def get_assessment_results_by_user_id(self, u_id):
        #returns the assement_result with the
        cur = self.conn.cursor()
        cur.execute('''
            SELECT
            ar.assessment_id,
            c.name AS competency_name,
            a.name AS assessment_name,
            ar.score,
            ar.date_taken
            FROM Assessment_Results AS ar
            JOIN Assessments AS a
            ON a.assessment_id = ar.assessment_id
            JOIN Competencies AS c
            ON c.competency_id = a.competency_id
            WHERE ar.user_id = ?       
            ORDER BY
            ar.assessment_id ASC,
            ar.date_taken ASC;
            ''',(u_id))
        rows = cur.fetchall()
        if rows is None:
            return None
        return rows

    def update_user_data(self, u_id, f_name, l_name, phone, email):
        cur = self.conn.cursor()
        cur.execute(
            """
            UPDATE Users
            SET f_name = ?, l_name = ?, phone = ?, email = ?
            WHERE user_id = ?
            """,
            (f_name, l_name, phone, email, u_id)
        )
        self.conn.commit()
        return cur.rowcount
    def load_user_by_id(self, user_id):
        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT
                user_id, f_name, l_name, phone, email, password_hash,
                creation_date, hire_date, user_type, active
            FROM Users
            WHERE user_id = ?
            """,
            (user_id,)
        )
        row = cur.fetchone()
        if row is None:
            return None

        return User(
            user_id=row[0],
            f_name=row[1],
            l_name=row[2],
            phone=row[3],
            email=row[4],
            password_hash=row[5],
            creation_date=row[6],
            hire_date=row[7],
            user_type=row[8],
            active=row[9]
        )

    def get_all_compentencies(self):
            cur = self.conn.cursor()
            cur.execute(
                """
                SELECT
                    competency_id, name
                FROM Competencies
                """)
            rows = cur.fetchall()
            if rows is None:
                return None
            else:
                return rows
    def get_compentency_by_id(self,c_id):
        cur = self.conn.cursor()
        cur.execute('''SELECT * FROM Competencies WHERE competency_id = ?''',(c_id,))
        row = cur.fetchone()
        if row is None:
            return None
        return row
    def create_new_competency(self, name):
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO Competencies (name) VALUES(?)''',(name,)
        )
        self.conn.commit()
        return cur.lastrowid
    def delete_assessment_result_byid(self,ar_id):
        cur = self.conn.cursor()
        cur.execute('''DELETE FROM Assessment_Results
        WHERE assessment_id = ?''',(ar_id,))
        self.conn.commit()
        print("Deleted Assessment Result:", ar_id, "rows affected (Assessment Results):", cur.rowcount)
        return cur.rowcount

        
    def delete_competency_cascade(self, c_id):
        cur = self.conn.cursor()
        try:
            cur.execute("BEGIN")

            # 1) Delete results tied to assessments for this competency
            cur.execute("""
                DELETE FROM Assessment_Results
                WHERE assessment_id IN (
                    SELECT assessment_id
                    FROM Assessments
                    WHERE competency_id = ?
                )
            """, (c_id,))

            # 2) Delete assessments for this competency
            cur.execute("""
                DELETE FROM Assessments
                WHERE competency_id = ?
            """, (c_id,))

            # 3) Delete the competency itself
            cur.execute("""
                DELETE FROM Competencies
                WHERE competency_id = ?
            """, (c_id,))

            self.conn.commit()
            print("Deleted competency:", c_id, "rows affected (competency):", cur.rowcount)
            return cur.rowcount

        except sqlite3.IntegrityError as e:
            self.conn.rollback()
            print("Delete blocked by FK constraint:", e)
            return 0
        except Exception as e:
            self.conn.rollback()
            print("DB error:", e)
            return 0
    def update_competency(self, c_id, data):
        cur = self.conn.cursor()
        cur.execute('''UPDATE Competencies SET name = ? WHERE competency_id = ? ''',(data,c_id)
        )
        self.conn.commit()
        return cur.lastrowid
    def add_new_assessment_result(self,u_id,a_id,manager_id,score):
        cur = self.conn.cursor()
        today = datetime.now().strftime("%Y-%m-%d")
        cur.execute(''' INSERT INTO Assessment_Results(user_id, assessment_id,date_taken, manager_id, score)
        VALUES(?,?,?,?,?)''',(u_id,a_id,today,manager_id,score)
        )
        self.conn.commit()
        return cur.lastrowid
    def get_assements_for_user(self,u_id):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT
            ar.assessment_id,
            a.name AS assessment_name,
            COALESCE(m.f_name || ' ' || m.l_name, '') AS manager_full_name,
            ar.score,
            ar.date_taken
        FROM Assessment_Results ar
            JOIN Users u
            ON u.user_id = ar.user_id
            JOIN Assessments a
            ON a.assessment_id = ar.assessment_id
            JOIN Competencies c
            ON c.competency_id = a.competency_id
            LEFT JOIN Users m
            ON m.user_id = ar.manager_id
        WHERE ar.user_id = ?
        AND u.active = 1          
        ORDER BY ar.date_taken DESC, ar.assessment_id;''',(u_id,))
        rows = cur.fetchall()
        if rows is None:
            return None
        return rows
    def get_user_competency_summary_for_user(self,u_id):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT
           COALESCE(u.f_name || ' ' || u.l_name, '') AS user_name,
            c.name AS competency_name,
            a.name AS assessment_name,
            ar.score,
            ar.date_taken
        FROM Competencies c
        CROSS JOIN Users u
        LEFT JOIN Assessments a
            ON a.competency_id = c.competency_id
        LEFT JOIN Assessment_Results ar
            ON ar.assessment_id = a.assessment_id
        AND ar.user_id = u.user_id
        WHERE u.user_id = ?
        AND a.name IS NOT NULL
        AND u.active = 1
        AND (
                ar.date_taken IS NULL
                OR ar.date_taken = (
                    SELECT MAX(ar2.date_taken)
                    FROM Assessment_Results ar2
                    JOIN Assessments a2
                    ON ar2.assessment_id = a2.assessment_id
                    WHERE ar2.user_id = u.user_id
                    AND a2.competency_id = c.competency_id
                )
            )
        ORDER BY c.competency_id;''',(u_id,))
        rows = cur.fetchall()
        if rows is None:
            return None
        return rows
    def get_competency_result_summary(self,c_id):
        cur = self.conn.cursor()
        cur.execute('''
        SELECT
            c.name AS competency_name,
            COALESCE(u.f_name || ' ' || u.l_name, '') AS user_name,
            a.name AS assessment_name,
            ar.score,
            ar.date_taken
        FROM Users u
        LEFT JOIN Assessment_Results ar
            ON ar.user_id = u.user_id
        LEFT JOIN Assessments a
            ON a.assessment_id = ar.assessment_id
        LEFT JOIN Competencies c
            ON c.competency_id = a.competency_id
        WHERE c.competency_id = ?
        AND u.active = 1
        AND (
            ar.date_taken IS NULL
            OR ar.date_taken = (
                SELECT MAX(ar2.date_taken)
                FROM Assessment_Results ar2
                JOIN Assessments a2
                    ON a2.assessment_id = ar2.assessment_id
                WHERE ar2.user_id = u.user_id
                    AND a2.competency_id = c.competency_id
            )
        )
        ORDER BY u.l_name, u.f_name;''',(c_id,))
        rows = cur.fetchall()
        if rows is None:
            return None
        return rows
    def deactivate_user_by_id(self,u_id):
        cur = self.conn.cursor()
        cur.execute('''
        UPDATE Users        
        SET active = 0
        WHERE user_id = ?''',(u_id))
        self.conn.commit()
        return cur.lastrowid
    def get_all_managers(self):
        cur = self.conn.cursor()
        cur.execute(
            '''
            SELECT
                user_id,
                COALESCE(u.f_name || ' ' || u.l_name, '') AS user_name,
                email
            FROM Users u
            WHERE user_type = 'manager'
            '''
        )
        rows = cur.fetchall()
        if rows is None:
            return None
        return rows
    def get_manager_by_id(self,u_id):
        cur = self.conn.cursor()
        cur.execute(
            '''
            SELECT
                user_id,
                COALESCE(u.f_name || ' ' || u.l_name, '') AS user_name,
                email
            FROM Users u
            WHERE user_type = 'manager'
            AND user_id = ?
            ''',(u_id,)
        )
        row = cur.fetchone()
        if row is None:
            return None

        return row
    


