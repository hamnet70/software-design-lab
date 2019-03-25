PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE person (
id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
age INTEGER
);
CREATE TABLE pet (
id INTEGER PRIMARY KEY,
name TEXT,
breed TEXT,
age INTEGER,
dead INTEGER
);
INSERT INTO pet VALUES(1,'Fido',NULL,NULL,NULL);
INSERT INTO pet VALUES(2,'Sonny Liston',NULL,NULL,NULL);
INSERT INTO pet VALUES(3,'Byrd',NULL,NULL,NULL);
CREATE TABLE person_pet (
person_id INTEGER,
pet_id INTEGER
);
COMMIT;
