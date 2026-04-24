/* Write your T-SQL query statement below */

WITH result AS (
    SELECT 
        reports_to, 
        reports_count, 
        average_age

    FROM (
        SELECT 
            reports_to, 
            COUNT(*) AS reports_count,
            ROUND(AVG(CAST(age AS FLOAT)), 0) AS average_age 
        FROM Employees
        GROUP BY reports_to
    )t

    WHERE reports_to IS NOT NULL
)

SELECT 
    e.employee_id, 
    e.name, 
    r.reports_count, 
    r.average_age 

FROM Employees e
RIGHT JOIN result r 
ON e.employee_id = r.reports_to
ORDER BY e.employee_id