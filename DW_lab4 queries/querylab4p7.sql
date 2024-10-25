SELECT 
    p.ProductID,
    p.ProductName,
    YEAR(o.OrderDate) AS Year,
    MONTH(o.OrderDate) AS Month,
    SUM(od.UnitPrice * od.Quantity) AS TotalSalesAmount,
    SUM(od.Quantity * od.UnitPrice * od.Discount / 100) AS TotalDiscountAmount
FROM 
    OrderDetails od, Orders o, Products p
WHERE 
    od.OrderID = o.OrderID
    AND od.ProductID = p.ProductID
GROUP BY 
    p.ProductID, p.ProductName, YEAR(o.OrderDate), MONTH(o.OrderDate);
