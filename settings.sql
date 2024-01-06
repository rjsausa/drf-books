-- settings.sql
CREATE DATABASE drfbooks;
CREATE USER drfbooksuser WITH PASSWORD 'drfbooks';
GRANT ALL PRIVILEGES ON DATABASE drfbooks TO drfbooksuser;

-- Example
-- CREATE DATABASE books;
-- CREATE USER booksuser WITH PASSWORD 'books';
-- GRANT ALL PRIVILEGES ON DATABASE books TO booksuser;
