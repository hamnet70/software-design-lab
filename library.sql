
CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    genre TEXT,
)

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
)

CREATE TABLE books_by_genre (
    book_id INTEGER,
    genre_id INTEGER
)