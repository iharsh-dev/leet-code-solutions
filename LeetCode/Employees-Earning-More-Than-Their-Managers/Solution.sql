1# Write your MySQL query statement below
2SELECT e.name AS Employee 
3FROM Employee e 
4JOIN Employee m 
5    ON e.managerId = m.Id
6WHERE e.salary > m.salary;