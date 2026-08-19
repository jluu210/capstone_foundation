import csv
import sqlite3
from pathlib import Path
from user import User
from db import *


def import_csv_wf(muser: User,db:Database):
    inserted_count = 0

    filename = input("Enter the CSV filename: ").strip()
    file_path = Path.cwd() / filename

    if not file_path.is_file():
        print(f"File not found: {file_path}")
        return False

    required_columns = {
        "user_id",
        "assessment_id",
        "date_taken",
        "score"
    }

    connection = None

    try:
        connection = sqlite3.connect("capstone.db")
        connection.execute("PRAGMA foreign_keys = ON")

        with file_path.open(
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as csv_file:

            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None:
                print("The CSV file does not contain a header row.")
                return False

            actual_columns = {
                column.strip()
                for column in reader.fieldnames
                if column is not None
            }

            missing_columns = required_columns - actual_columns

            if missing_columns:
                print(
                    "The CSV file is missing these columns: "
                    + ", ".join(sorted(missing_columns))
                )
                return False

            with connection:
                for line_number, row in enumerate(reader, start=2):
                    try:
                        user_id = int(row["user_id"].strip())
                        assessment_id = int(row["assessment_id"].strip())
                        score = int(row["score"].strip())
                        date_taken = row["date_taken"].strip()
                        manager_id = muser.user_id

                        if score < 0 or score > 4:
                            raise ValueError(
                                f"score must be between 0 and 4. Line Number: {line_number}"
                            )

                        if not date_taken:
                            raise ValueError(
                                f"date_taken cannot be empty. Line Number: {line_number}"
                            )
                        if not db.user_exists(user_id):
                            raise ValueError(
                                f"User not found for ID: {user_id} on Line: {line_number}"
                            )

                        connection.execute(
                            '''
                            INSERT INTO Assessment_Results
                                (
                                    user_id,
                                    assessment_id,
                                    date_taken,
                                    manager_id,
                                    score
                                )
                            VALUES (?, ?, ?, ?, ?)
                            ''',
                            (
                                user_id,
                                assessment_id,
                                date_taken,
                                manager_id,
                                score
                            )
                        )

                        inserted_count += 1

                    except ValueError as error:
                        print(f"Import failed: {error}")
                        return False

    except sqlite3.IntegrityError as error:
        print(f"Database constraint error: {error}")
        return False

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False

    except Exception as error:
        print(f"Import failed: {error}")
        return False

    finally:
        if connection is not None:
            connection.close()

    print(
        f"Successfully imported {inserted_count} "
        f"assessment result(s)."
    )

    return True