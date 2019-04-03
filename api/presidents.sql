/* Practicing my SQL skills */

CREATE TABLE presidents (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    total_terms INTEGER,
    years_served INTEGER,
    wife_first_name TEXT
);

insert into presidents values (0, "George", "Washington", 2, 8, "Martha");
insert into presidents values (1, "John", "Adams", 1, 4, "Abigail");
insert into presidents values (2, "Thomas", "Jefferson", 2, 8, "None");
insert into presidents values (3, "James", "Madison", 2, 8, "Dolley");
insert into presidents values (4, "James", "Monroe", 2, 8, "Elizabeth");
insert into presidents values (5, "John Quincy", "Adams", 1, 4, "Louisa");
insert into presidents values (6, "Andrew", "Jackson", 2, 8, "Rachel");
insert into presidents values (7, "Martin", "Van Buren", 1, 4, "Hannah");