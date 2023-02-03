TRUNCATE TABLE contact;

ALTER SEQUENCE constact_id_seq RESTART WITH 1;

INSERT INTO contact(name, email) VALUES('Orlando', 'orlando@gmail.com');
INSERT INTO contact(name, email) VALUES('Samantha', 'samantha@gmail.com');
INSERT INTO contact(name, email) VALUES('Eddie', 'eddie@gmail.com');
INSERT INTO contact(name, email) VALUES('Alexia', 'alexia@gmail.com');
INSERT INTO contact(name, email) VALUES('Devan', 'devan@gmail.com');