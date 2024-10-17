import pyodbc
import time
import matplotlib.pyplot as plt

con = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-B0IU82M\\SQLEXPRESS;"  
    "Database=Northwind_Rabbiya;"  
    "Trusted_Connection=yes;")
cur = con.cursor()
pk_qs = {
    "Order by ID": "SELECT * FROM Orders WHERE OrderID = 10248",
    "Customer by ID": "SELECT * FROM Customers WHERE CustomerID = 'ALFKI'",
    "Supplier by ID": "SELECT * FROM Suppliers WHERE SupplierID = 1",
    "Product by ID": "SELECT * FROM Products WHERE ProductID = 1",
    "Employee by ID": "SELECT * FROM Employees WHERE EmployeeID = 1"
}
n_pk_qs = {
    "Customer by Name": "SELECT * FROM Customers WHERE CompanyName = 'Alfreds Futterkiste'",
    "Shipper by Name": "SELECT * FROM Shippers WHERE CompanyName = 'Speedy Express'",
    "Order by Date": "SELECT * FROM Orders WHERE OrderDate = '1996-07-04'",
    "Order by Cust Name": "SELECT * FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID WHERE CompanyName = 'Alfreds Futterkiste'",
    "Order by Shipper Name": "SELECT * FROM Orders INNER JOIN Shippers ON Orders.ShipVia = Shippers.ShipperID WHERE CompanyName = 'Speedy Express'"
}
pk_times = {}
for q_name, q in pk_qs.items():
    start = time.time()
    cur.execute(q)
    cur.fetchall()
    end = time.time()
    pk_times[q_name] = (end - start) * 1000 
n_pk_times = {}
for q_name, q in n_pk_qs.items():
    start = time.time()
    cur.execute(q)
    cur.fetchall()
    end = time.time()
    n_pk_times[q_name] = (end - start) * 1000  
con.close()
all_times = {**pk_times, **n_pk_times}
plt.figure(figsize=(10, 6))
plt.bar(all_times.keys(), all_times.values(), color=['#F08080' if 'Order' in k else '#9370DB' for k in all_times.keys()])
plt.xticks(rotation=90)
plt.xlabel('Queries')
plt.ylabel('Execution Time (ms)')
plt.title('Execution Times: PK vs Non-PK Queries')
plt.tight_layout()
plt.show()

