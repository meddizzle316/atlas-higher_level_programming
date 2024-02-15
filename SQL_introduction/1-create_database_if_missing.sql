-- an sql script that creates a database
-- if none exists

IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'hbtn_0c_0')
BEGIN
    CREATE DATABASE hbtn_0c_0;
END
