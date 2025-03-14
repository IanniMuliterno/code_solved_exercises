-- credits to leet code
--A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary
--in the top three unique salaries for that department.

--Write a solution to find the employees who are high earners in each of the departments.

--Return the result table in any order.

with aux_tb as (
select d.name as Department, 
e.name as Employee, salary as Salary ,dense_rank() over (partition by d.name order by salary desc) as rank_salary
from department d
left join employee e on d.id = e.departmentId
)

select Department, Employee, Salary
from aux_tb
where rank_salary < 4
