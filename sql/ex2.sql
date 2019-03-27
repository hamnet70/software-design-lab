/* This is the chapter 2 exercise from Zed Shaw */

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);

CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    nickname TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);

CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
);


insert into person values (0, "Kelly", "Hammond", 48);
insert into person values (1, "Hasib", "Ikramullah", 43);
insert into person values (2, "Kim", "Roessler", 50);
insert into person values (3, "Martha", "Hammond", 78);

insert into pet values (0, "Spot", "Boxer", 3, 0);
insert into pet values (1, "Fifi", "Poodle", 7, 0);
insert into pet values (2, "Popeye", "Hamster", 1, 1);

insert into person_pet values (0, 2);
insert into person_pet values (1, 0);
insert into person_pet values (2, 1);
insert into person_pet values (3, 2);