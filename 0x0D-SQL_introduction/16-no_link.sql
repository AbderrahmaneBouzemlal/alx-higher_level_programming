-- lists all the records with names
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC, name;
