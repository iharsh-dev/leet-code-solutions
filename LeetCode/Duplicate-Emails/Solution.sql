1# Write your MySQL query statement below
2SELECT email FROM Person
3GROUP BY email 
4HAVING COUNT(*) > 1;