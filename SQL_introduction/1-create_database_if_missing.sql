-- an sql script that creates a database
-- if none exists

IF hbtn_0c_0_ID('dms') IS NOT NULL
-- IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'hbtn_0c_0')
BEGIN
    CREATE DATABASE hbtn_0c_0;
END
