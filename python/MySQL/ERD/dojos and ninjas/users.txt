INSERT INTO users (first_name, last_name, email)
values ('John', 'Wick', 'coolguy@eliminator.com')

INSERT INTO users (first_name, last_name, email)
values ('John', 'Sheridan', 'commander@B5.com')

INSERT INTO users (first_name, last_name, email)
values ('Welsys', 'Unknown', 'dragonapprentice@technomage.com')


SELECT *
FROM users;

SELECT *
FROM users
WHERE (id = 1) AND (email = 'coolguy@eliminator.com');

SELECT *
FROM users
WHERE (id = 3);


UPDATE users
SET last_name = 'Pancakes';

DELETE FROM users WHERE id = 2;

SELECT *
FROM users
ORDER BY first_name DESC;