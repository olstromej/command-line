DROP TABLE IF EXISTS contact;

CREATE TABLE contact (
id SERIAL PRIMARY KEY,
name VARCHAR(255),
email VARCHAR(255)
);