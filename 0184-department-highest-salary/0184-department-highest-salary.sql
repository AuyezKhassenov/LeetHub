
SELECT
Department,
Employee,
Salary 
FROM
(SELECT e.name Employee, salary Salary,d.name Department, max(salary) OVER(PARTITION BY departmentId) max_salary FROM Employee e JOIN Department d
ON e.departmentId = d.id) f
WHERE Salary = max_salary