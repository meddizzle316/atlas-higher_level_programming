-- Write a script that lists all records of the table second_table of 
-- the database hbtn_0c_0 in your MySQL server.

SELECT * FROM score, name
WHERE name IS NOT NULL AND name != ''
ORDER BY score;
