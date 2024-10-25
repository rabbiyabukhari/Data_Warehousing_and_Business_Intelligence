SELECT 
    p.ProductName,
    YEAR(o.OrderDate) AS Year,
    MONTH(o.OrderDate) AS Month,
    SUM(od.UnitPrice * od.Quantity) AS TotalSales,
    LAG(SUM(od.UnitPrice * od.Quantity)) OVER (PARTITION BY p.ProductID ORDER BY YEAR(o.OrderDate), MONTH(o.OrderDate)) AS PreviousMonthSales
FROM 
    OrderDetails od
JOIN 
    Orders o ON od.OrderID = o.OrderID
JOIN 
    Products p ON od.ProductID = p.ProductID
GROUP BY 
    p.ProductName, p.ProductID, YEAR(o.OrderDate), MONTH(o.OrderDate)
ORDER BY 
    Year, Month;
