
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR,
    director VARCHAR,
    year INTEGER
);

INSERT INTO movies (title, director, year) VALUES ("Field of Dreams", "Robinson", 1989);
INSERT INTO movies (title, director, year) VALUES ("Annie Hall", "Allen", 1977);
INSERT INTO movies (title, director, year) VALUES ("Avatar", "Cameron", 2009);


CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    genre_name VARCHAR 
);

INSERT INTO genres (genre_name) VALUES ("Horror");
INSERT INTO genres (genre_name) VALUES ("Drama");
INSERT INTO genres (genre_name) VALUES ("Comedy");
INSERT INTO genres (genre_name) VALUES ("Sports");


CREATE TABLE genre_connect (
    id INTEGER PRIMARY KEY,
    dvd_id INTEGER,
    genre_id INTEGER
);

INSERT INTO genre_connect (dvd_id, genre_id) VALUES (1, 2);
INSERT INTO genre_connect (dvd_id, genre_id) VALUES (1, 4);
INSERT INTO genre_connect (dvd_id, genre_id) VALUES (2, 3);
INSERT INTO genre_connect (dvd_id, genre_id) VALUES (3, 2);

