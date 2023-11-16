-- create the database hbtn_0d_2 and user user_0d_2.
-- creating the databse first
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--creating the user called user_0d_2 with password user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants select to the user 'user_0d_2' on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2 TO user_0d_2@localhost;
