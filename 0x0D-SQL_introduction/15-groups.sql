--  a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
SELECT score,  COUNT(*) as 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC;
