/* Seeing if I can create tables from scratch without looking */

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    section TEXT
);

CREATE TABLE assignments (
    id INTEGER PRIMARY KEY,
    due_date TEXT,
    title TEXT,
    total_points INTEGER
);

CREATE TABLE gradebook (
    students_id INTEGER,
    assignments_id INTEGER,
    grade_received INTEGER
);


