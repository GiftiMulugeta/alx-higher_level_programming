--  a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
SELECT SUM(TABLE_ROWS) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'hbtn_0c_0';
