SELECT 
    c.CategoryID,
    c.CategoryName,
    YEAR(o.OrderDate) AS Year,
    MONTH(o.OrderDate) AS Month,
    SUM(od.UnitPrice * od.Quantity) AS TotalSales,
    SUM(SUM(od.UnitPrice * od.Quantity)) OVER (PARTITION BY c.CategoryID, YEAR(o.OrderDate) ORDER BY MONTH(o.OrderDate)) AS YearToDateSales
FROM 
    OrderDetails od, Orders o, Products p, Categories c
WHERE 
    od.OrderID = o.OrderID
    AND od.ProductID = p.ProductID
    AND p.CategoryID = c.CategoryID
GROUP BY 
    c.CategoryID, c.CategoryName, YEAR(o.OrderDate), MONTH(o.OrderDate);
