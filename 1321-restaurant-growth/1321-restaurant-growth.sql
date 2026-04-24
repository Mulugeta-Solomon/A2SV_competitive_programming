/* Write your T-SQL query statement below */
WITH growth AS (
    SELECT 
        visited_on,
        PrevDay,
        SUM(t.amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount, 
        ROUND(AVG(CAST(amount AS FLOAT)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ), 2) AS average_amount 

    FROM (
        SELECT 
            visited_on,
            LAG(visited_on, 6) OVER(ORDER BY visited_on) AS PrevDay,
            SUM(amount) AS amount
        FROM Customer 
        GROUP BY visited_on
    ) AS t
)

SELECT 
    g.visited_on, 
    g.amount, 
    g.average_amount 

FROM growth AS g

WHERE DATEDIFF(DAY, g.PrevDAY, g.visited_on) IS NOT NULL