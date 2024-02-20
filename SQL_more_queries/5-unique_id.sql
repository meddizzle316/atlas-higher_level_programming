-- Write a script that creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT iDENTITY(1, 1),
    name VARCHAR(256)
)
