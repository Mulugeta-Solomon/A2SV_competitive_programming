/* Write your T-SQL query statement below */

SELECT name AS results 
FROM (
    SELECT TOP 1 u.name 
    FROM Users AS u
    JOIN MovieRating AS mr
    ON mr.user_id = u.user_id
    GROUP BY u.name
    ORDER BY COUNT(*) DESC, u.name
)t

UNION ALL 
SELECT title 
FROM (
    SELECT TOP 1 m.title
    FROM Movies AS m
    JOIN MovieRating AS mr
    ON mr.movie_id = m.movie_id
    WHERE MONTH(created_at) = '2' AND YEAR(created_at) = '2020'
    GROUP BY m.title
    ORDER BY AVG(CAST(mr.rating AS FLOAT)) DESC, m.title
)t1

