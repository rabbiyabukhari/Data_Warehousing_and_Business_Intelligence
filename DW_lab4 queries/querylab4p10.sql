WITH EmployeeSales AS (
    SELECT 
        e.EmployeeID,
        e.ReportsTo,
        SUM(od.UnitPrice * od.Quantity) AS TotalSales
    FROM 
        Orders o, OrderDetails od, Employees e
    WHERE 
        o.OrderID = od.OrderID
        AND o.EmployeeID = e.EmployeeID
        AND YEAR(o.OrderDate) = 1997
    GROUP BY 
        e.EmployeeID, e.ReportsTo
)
SELECT 
    e.EmployeeID,
    e.LastName,
    e.FirstName,
    es.TotalSales AS PersonalSales,
    COALESCE(subordinate_sales.TotalSales, es.TotalSales) AS TotalWithSubordinatesSales
FROM 
    EmployeeSales es, Employees e
LEFT JOIN 
    (SELECT ReportsTo, SUM(TotalSales) AS TotalSales FROM EmployeeSales GROUP BY ReportsTo) subordinate_sales
    ON e.EmployeeID = subordinate_sales.ReportsTo
WHERE 
    es.EmployeeID = e.EmployeeID;