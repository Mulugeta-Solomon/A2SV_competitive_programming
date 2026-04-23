/* Write your T-SQL query statement below */

SELECT Employee.name
FROM (
    SELECT 
        e1.id,
        COUNT(e1.id) AS count

    FROM Employee e1
    INNER JOIN Employee e2
    ON e1.id = e2.managerId
    GROUP BY e1.id
    HAVING COUNT(e1.id) >= 5
)t, Employee

WHERE t.id =　Employee.id 
