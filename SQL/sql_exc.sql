/*
A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.
*/
with table1 as
(select employee.*, department.name as Department from employee inner join department 
on employee.departmentId=department.id)

select Department, name as Employee, salary as Salary from 
(select *,dense_rank() over(partition by departmentId order by salary desc) as rank1 from table1)t
where rank1<=3