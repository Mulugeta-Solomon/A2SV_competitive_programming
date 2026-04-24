/* Write your T-SQL query statement below */
WITH all_id AS (
    SELECT requester_id AS id 
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id 
    FROM RequestAccepted
)


SELECT TOP 1
    id, 
    COUNT(*) AS num
FROM all_id
GROUP BY id
ORDER BY COUNT(*) DESC



