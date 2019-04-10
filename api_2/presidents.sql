/* Practicing my SQL skills */

CREATE TABLE presidents (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    terms INTEGER,
    o INTEGER,
    wife TEXT
    );

CREATE TABLE blogs (
    id INTEGER PRIMARY KEY,
    username TEXT,
    posttime TEXT,
    post TEXT
    );

insert into presidents values (0, "George", "Washington", 2, 1, "Martha");
insert into presidents values (1, "John", "Adams", 1, 2, "Abigail");
insert into presidents values (2, "Thomas", "Jefferson", 2, 3, "None");
insert into presidents values (3, "James", "Madison", 2, 4, "Dolley");
insert into presidents values (4, "James", "Monroe", 2, 5, "Elizabeth");
insert into presidents values (5, "John Quincy", "Adams", 1, 6, "Louisa");
insert into presidents values (6, "Andrew", "Jackson", 2, 7, "Rachel");
insert into presidents values (7, "Martin", "Van Buren", 1, 8, "Hannah"); 

