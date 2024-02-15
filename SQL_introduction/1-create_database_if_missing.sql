-- an sql script that creates a database
-- if none exists
-- IF NOT EXISTS ( name FROM master.dbo.sysdatabases WHERE name = N'hbtn_0c_0')

-- IF DB_ID('hbtn_0c_0_ID') IS NOT NULL
-- BEGIN
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
-- END
