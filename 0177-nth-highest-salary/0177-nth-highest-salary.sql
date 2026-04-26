CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
        WITH rn AS (
            SELECT 
                t.salary, 
                ROW_NUMBER() OVER(ORDER BY t.salary DESC) AS salary_rank 
            FROM (
                SELECT DISTINCT 
                    e.salary
                FROM Employee AS e
            ) AS t
        )

        SELECT rn.salary 
        FROM rn 
        WHERE rn.salary_rank = N
      
  );
END;
$$ LANGUAGE plpgsql;