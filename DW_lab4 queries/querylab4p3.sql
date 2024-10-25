SELECT 
    TOP 3 
    e.EmployeeID, 
    e.LastName, 
    e.FirstName, 
    SUM(od.UnitPrice * od.Quantity) AS TotalSales
FROM 
    Orders o, OrderDetails od, Employees e
WHERE 
    o.OrderID = od.OrderID
    AND o.EmployeeID = e.EmployeeID
GROUP BY 
    e.EmployeeID, e.LastName, e.FirstName
ORDER BY 
    TotalSales DESC;
