/* Write your T-SQL query statement below */

WITH lookup AS (
    SELECT 
        name, 
        COALESCE(referee_id, 1) AS id
    
    FROM Customer
) 


SELECT name 
FROM lookup
WHERE id != 2