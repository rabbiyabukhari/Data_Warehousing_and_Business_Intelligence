SELECT 
    c.CategoryID,
    c.CategoryName,
    YEAR(o.OrderDate) AS Year,
    MONTH(o.OrderDate) AS Month,
    SUM(od.UnitPrice * od.Quantity) AS TotalSales,
    AVG(SUM(od.UnitPrice * od.Quantity)) OVER (PARTITION BY c.CategoryID ORDER BY YEAR(o.OrderDate), MONTH(o.OrderDate) ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS MovingAvgSales
FROM 
    OrderDetails od, Orders o, Products p, Categories c
WHERE 
    od.OrderID = o.OrderID
    AND od.ProductID = p.ProductID
    AND p.CategoryID = c.CategoryID
GROUP BY 
    c.CategoryID, c.CategoryName, YEAR(o.OrderDate), MONTH(o.OrderDate);