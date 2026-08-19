
-- Seed dummy data


-- Clean slate 
-- DELETE FROM Assessment_Results;
-- DELETE FROM Assessments;
-- DELETE FROM Competencies;
-- DELETE FROM Users;

-- -------------------------
-- Users (20 total; 5 managers)
-- -------------------------
INSERT INTO Users (f_name, l_name, phone, email, password_hash, hire_date, user_type, active)
VALUES
('Ava','Johnson','555-1001','ava.johnson@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-01-10','manager',1),
('Noah','Williams','555-1002','noah.williams@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-02-14','manager',1),
('Mia','Brown','555-1003','mia.brown@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-03-18','manager',1),
('Ethan','Jones','555-1004','ethan.jones@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-04-22','manager',1),
('Sophia','Garcia','555-1005','sophia.garcia@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-05-26','manager',1),

('Liam','Miller','555-2001','liam.miller@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-03','user',1),
('Emma','Davis','555-2002','emma.davis@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-07','user',1),
('Oliver','Rodriguez','555-2003','oliver.rodriguez@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-11','user',1),
('Charlotte','Martinez','555-2004','charlotte.martinez@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-15','user',1),
('James','Hernandez','555-2005','james.hernandez@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-19','user',1),
('Amelia','Lopez','555-2006','amelia.lopez@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-23','user',1),
('Benjamin','Gonzalez','555-2007','benjamin.gonzalez@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-06-27','user',1),
('Harper','Wilson','555-2008','harper.wilson@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-01','user',1),
('Elijah','Anderson','555-2009','elijah.anderson@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-05','user',1),
('Emily','Thomas','555-2010','emily.thomas@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-09','user',1),
('Lucas','Taylor','555-2011','lucas.taylor@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-13','user',1),
('Avery','Moore','555-2012','avery.moore@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-17','user',1),
('Henry','Jackson','555-2013','henry.jackson@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-21','user',1),
('Ella','Martin','555-2014','ella.martin@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-25','user',1),
('Daniel','Lee','555-2015','daniel.lee@example.com','$2b$12$x9EpWE06Sb1DdJ5Ql1h.F.abuPz6IqNDhsnJq1FChF8zNIhGeILna','2024-07-29','user',1);

-- -------------------------
-- Competencies (25 total
-- -------------------------
INSERT INTO Competencies (name)
VALUES
('Computer Anatomy'),
('Data Types'),
('Variables'),
('Functions'),
('Boolean Logic'),
('Conditionals'),
('Loops'),
('Data Structures'),
('Lists'),
('Dictionaries'),
('Working with Files'),
('Exception Handling'),
('Quality Assurance (QA)'),
('Object-Oriented Programming'),
('Recursion'),
('Databases'),

('Debugging'),
('Version Control (Git)'),
('Code Style & Readability'),
('Testing Basics'),
('API Usage'),
('HTTP & REST'),
('Regular Expressions'),
('SQL Joins'),
('Performance Basics'),
('Refactoring');

-- -------------------------
-- Create Assessments for each competency
-- (You need Assessments rows so Assessment_Results can reference them.)
-- -------------------------
INSERT INTO Assessments (competency_id, name)
SELECT competency_id, name || ' - Assessment 1'
FROM Competencies;

---------------------------



INSERT INTO Assessment_Results (user_id, assessment_id, date_taken, manager_id, score)
VALUES
-- Student 1 (user_id=6)
(6, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Computer Anatomy')), '2025-01-10', 1, 3),
(6, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Data Types')), '2025-01-10', 1, 2),
(6, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Loops')), '2025-01-10', 1, 4),

-- Student 2 (user_id=7)
(7, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Functions')), '2025-01-12', 2, 4),
(7, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Conditionals')), '2025-01-12', 2, 3),

-- Student 3 (user_id=8)
(8, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Boolean Logic')), '2025-01-14', 3, 1),
(8, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Data Structures')), '2025-01-14', 3, 2),
(8, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Lists')), '2025-01-14', 3, 3),

-- Student 4 (user_id=9)
(9, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Dictionaries')), '2025-01-16', 4, 2),
(9, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Exception Handling')), '2025-01-16', 4, 0),

-- Student 5 (user_id=10)
(10, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Working with Files')), '2025-01-18', 5, 4),

-- Student 6 (user_id=11)
(11, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Object-Oriented Programming')), '2025-01-20', 1, 3),
(11, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Quality Assurance (QA)')), '2025-01-20', 1, 2),
(11, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Testing Basics')), '2025-01-20', 1, 3),

-- Student 7 (user_id=12)
(12, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Recursion')), '2025-01-22', 2, 2),
(12, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Databases')), '2025-01-22', 2, 1),

-- Student 8 (user_id=13)
(13, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='SQL Joins')), '2025-01-24', 3, 3),
(13, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Regular Expressions')), '2025-01-24', 3, 2),

-- Student 9 (user_id=14)
(14, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Version Control (Git)')), '2025-01-26', 4, 4),
(14, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Debugging')), '2025-01-26', 4, 3),

-- Student 10 (user_id=15)
(15, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Code Style & Readability')), '2025-01-28', 5, 2),

-- Student 11 (user_id=16)
(16, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Performance Basics')), '2025-01-30', 1, 1),
(16, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Refactoring')), '2025-01-30', 1, 2),
(16, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Data Types')), '2025-01-30', 1, 3),

-- Student 12 (user_id=17)
(17, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='API Usage')), '2025-02-01', 2, 4),
(17, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='HTTP & REST')), '2025-02-01', 2, 3),

-- Student 13 (user_id=18)
(18, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Loops')), '2025-02-03', 3, 0),
(18, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Variables')), '2025-02-03', 3, 2),

-- Student 14 (user_id=19)
(19, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Conditionals')), '2025-02-05', 4, 4),
(19, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Exception Handling')), '2025-02-05', 4, 2),

-- Student 15 (user_id=20)
(20, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Data Structures')), '2025-02-07', 5, 4),
(20, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Working with Files')), '2025-02-07', 5, 1),
(20, (SELECT assessment_id FROM Assessments WHERE competency_id = (SELECT competency_id FROM Competencies WHERE name='Dictionaries')), '2025-02-07', 5, 3);
