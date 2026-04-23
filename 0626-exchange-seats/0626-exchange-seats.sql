/* Write your T-SQL query statement below */

SELECT 
    CASE 
        WHEN id % 2 = 1 AND id != (SELECT MAX(s.id) FROM Seat s) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id 
    END AS id, 
    student

FROM Seat
ORDER BY id