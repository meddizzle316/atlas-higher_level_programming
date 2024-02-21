-- Write a script that lists all cities contained in the database hbtn_0d_usa.

SELECT cities.*, states.name AS "name"
FROM cities
JOIN states ON cities.name = cities.id;
