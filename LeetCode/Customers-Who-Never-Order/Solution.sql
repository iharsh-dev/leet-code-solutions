1# Write your MySQL query statement below
2SELECT name AS Customers FROM Customers c
3LEFT JOIN Orders o
4ON o.customerId = c.id
5WHERE o.customerID is NULL