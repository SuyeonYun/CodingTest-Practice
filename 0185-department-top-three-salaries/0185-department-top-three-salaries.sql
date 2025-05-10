# Write your MySQL query statement below

SELECT D.name AS Department, cte.name AS Employee, cte.salary AS Salary
FROM(
    SELECT 
        *, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk 
    FROM Employee           
    ) cte
LEFT JOIN Department D ON cte.departmentId = D.id
WHERE rk <= 3;
