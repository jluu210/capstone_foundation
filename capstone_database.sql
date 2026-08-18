-- Creates Databases for Competency Tracking Tool

PRAGMA foreign_keys = ON;

-- Users
CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name TEXT NOT NULL,
    l_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    creation_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    hire_date TEXT NOT NULL,
    user_type TEXT NOT NULL CHECK (user_type IN ('user','manager')),
    active INTEGER NOT NULL DEFAULT 1
);

-- Competencies
CREATE TABLE IF NOT EXISTS Competencies(
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    date_added TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Assessments
CREATE TABLE IF NOT EXISTS Assessments(
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    date_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_assessments_competency
      FOREIGN KEY (competency_id) REFERENCES Competencies(competency_id)
      ON UPDATE CASCADE
      ON DELETE RESTRICT
);

-- ASSESSMENT RESULTS
CREATE TABLE IF NOT EXISTS Assessment_Results (
  result_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  assessment_id INTEGER NOT NULL,
  date_taken TEXT NOT NULL,
  manager_id INTEGER NULL,
  score INTEGER NOT NULL,
 
  CONSTRAINT fk_results_user
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_results_assessment
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_results_manager
    FOREIGN KEY (manager_id) REFERENCES Users(user_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL,

  CONSTRAINT chk_assessment_results_score
    CHECK (score >= 0 AND score <= 4)
);