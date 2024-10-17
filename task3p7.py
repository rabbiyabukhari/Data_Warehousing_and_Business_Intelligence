import pyodbc
import pandas as pd
import os

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-B0IU82M\\SQLEXPRESS;" 
    "Database=Northwind_Rabbiya;"         
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
def load_products_from_csv(file_path):
    df = pd.read_csv(file_path)
    columns = 'ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued'
    placeholders = ', '.join('?' * 10)
    sql_insert_query = f"INSERT INTO Products ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        product_id = int(row['ProductID']) if 'ProductID' in df.columns and pd.notnull(row['ProductID']) else None
        product_name = str(row['ProductName']).strip() if 'ProductName' in df.columns and pd.notnull(row['ProductName']) else None
        supplier_id = int(row['SupplierID']) if 'SupplierID' in df.columns and pd.notnull(row['SupplierID']) else None
        category_id = int(row['CategoryID']) if 'CategoryID' in df.columns and pd.notnull(row['CategoryID']) else None
        quantity_per_unit = str(row['QuantityPerUnit']).strip() if 'QuantityPerUnit' in df.columns and pd.notnull(row['QuantityPerUnit']) else None
        unit_price = float(row['UnitPrice']) if 'UnitPrice' in df.columns and pd.notnull(row['UnitPrice']) else None
        units_in_stock = int(row['UnitsInStock']) if 'UnitsInStock' in df.columns and pd.notnull(row['UnitsInStock']) else None
        units_on_order = int(row['UnitsOnOrder']) if 'UnitsOnOrder' in df.columns and pd.notnull(row['UnitsOnOrder']) else None
        reorder_level = int(row['ReorderLevel']) if 'ReorderLevel' in df.columns and pd.notnull(row['ReorderLevel']) else None
        discontinued = int(row['Discontinued']) if 'Discontinued' in df.columns and pd.notnull(row['Discontinued']) else None

        cursor.execute(sql_insert_query, 
                       (product_id, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued))
    conn.commit()

def load_orders_from_csv(file_path):
    df = pd.read_csv(file_path)
    columns = 'OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry'
    placeholders = ', '.join('?' * 14)
    sql_insert_query = f"INSERT INTO Orders ({columns}) VALUES ({placeholders})"

def load_orders_from_csv(file_path):
    df = pd.read_csv(file_path)
    columns = 'OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry'
    placeholders = ', '.join('?' * 14)
    sql_insert_query = f"INSERT INTO Orders ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        order_id = int(row['OrderID']) if 'OrderID' in df.columns and pd.notnull(row['OrderID']) else None
        customer_id = str(row['CustomerID']).strip() if 'CustomerID' in df.columns and pd.notnull(row['CustomerID']) else None
        employee_id = int(row['EmployeeID']) if 'EmployeeID' in df.columns and pd.notnull(row['EmployeeID']) else None
        order_date = pd.to_datetime(row['OrderDate']) if 'OrderDate' in df.columns and pd.notnull(row['OrderDate']) else None
        required_date = pd.to_datetime(row['RequiredDate']) if 'RequiredDate' in df.columns and pd.notnull(row['RequiredDate']) else None
        shipped_date = pd.to_datetime(row['ShippedDate']) if 'ShippedDate' in df.columns and pd.notnull(row['ShippedDate']) else None
        ship_via = int(row['ShipVia']) if 'ShipVia' in df.columns and pd.notnull(row['ShipVia']) else None
        freight = float(row['Freight']) if 'Freight' in df.columns and pd.notnull(row['Freight']) else None
        ship_name = str(row['ShipName']).strip() if 'ShipName' in df.columns and pd.notnull(row['ShipName']) else None
        ship_address = str(row['ShipAddress']).strip() if 'ShipAddress' in df.columns and pd.notnull(row['ShipAddress']) else None
        ship_city = str(row['ShipCity']).strip() if 'ShipCity' in df.columns and pd.notnull(row['ShipCity']) else None
        ship_region = str(row['ShipRegion']).strip() if 'ShipRegion' in df.columns and pd.notnull(row['ShipRegion']) else None
        ship_postal_code = str(row['ShipPostalCode']).strip() if 'ShipPostalCode' in df.columns and pd.notnull(row['ShipPostalCode']) else None
        ship_country = str(row['ShipCountry']).strip() if 'ShipCountry' in df.columns and pd.notnull(row['ShipCountry']) else None
        cursor.execute(sql_insert_query, 
                       (order_id, customer_id, employee_id, order_date, required_date, shipped_date, ship_via, freight, ship_name, ship_address, ship_city, ship_region, ship_postal_code, ship_country))
    conn.commit()
def main():
    csv_path = r"C:\Users\Rabbiya\Desktop\DW LAB\DW LAB\northwind"  
    """ # Products data loading
    products_file = "Products.csv"
    products_path = os.path.join(csv_path, products_file)
    load_products_from_csv(products_path)
    """
    orders_file = "Orders.csv"
    orders_path = os.path.join(csv_path, orders_file)
    load_orders_from_csv(orders_path)
    conn.close()
main()
