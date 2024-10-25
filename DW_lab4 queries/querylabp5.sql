WITH TotalSales AS (
    SELECT 
        c.Country, 
        SUM(od.UnitPrice * od.Quantity) AS CountrySales
    FROM 
        Orders o, OrderDetails od, Customers c
    WHERE 
        o.OrderID = od.OrderID
        AND o.CustomerID = c.CustomerID
    GROUP BY 
        c.Country
),
CumulativeSales AS (
    SELECT 
        Country, 
        CountrySales, 
        SUM(CountrySales) OVER (ORDER BY CountrySales DESC) AS CumulativeSales,
        SUM(CountrySales) OVER () AS TotalSales
    FROM 
        TotalSales
)
SELECT 
    Country, 
    CountrySales
FROM 
    CumulativeSales
WHERE 
    CumulativeSales / NULLIF(TotalSales, 0) <= 0.5;
