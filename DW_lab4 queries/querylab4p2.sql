WITH MonthlySales AS (
    SELECT 
        p.ProductID,
        p.ProductName,
        YEAR(o.OrderDate) AS Year,
        MONTH(o.OrderDate) AS Month,
        SUM(od.UnitPrice * od.Quantity) AS TotalSales
    FROM 
        OrderDetails od, Orders o, Products p
    WHERE 
        od.OrderID = o.OrderID
        AND od.ProductID = p.ProductID
    GROUP BY 
        p.ProductID, p.ProductName, YEAR(o.OrderDate), MONTH(o.OrderDate)
)
SELECT 
    ProductName,
    Year,
    Month,
    TotalSales AS CurrentMonthSales,
    LAG(TotalSales) OVER (PARTITION BY ProductID ORDER BY Year, Month) AS PreviousMonthSales
FROM 
    MonthlySales
ORDER BY 
    Year, Month;
