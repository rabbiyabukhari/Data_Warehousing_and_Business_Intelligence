SELECT
    e.EmployeeID,
    e.LastName,
    e.FirstName,
    YEAR(o.OrderDate) AS Year,
    SUM(od.UnitPrice * od.Quantity) AS TotalSales,
    AVG(SUM(od.UnitPrice * od.Quantity)) OVER (PARTITION BY e.EmployeeID, YEAR(o.OrderDate)) AS AvgMonthlySales
FROM 
    Orders o, OrderDetails od, Employees e
WHERE 
    o.OrderID = od.OrderID
    AND o.EmployeeID = e.EmployeeID
GROUP BY 
    e.EmployeeID, e.LastName, e.FirstName, YEAR(o.OrderDate), MONTH(o.OrderDate);