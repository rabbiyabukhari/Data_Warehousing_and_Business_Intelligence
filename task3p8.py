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
def check_customer_exists(customer_id):
    cursor.execute("SELECT COUNT(1) FROM Customers WHERE CustomerID = ?", customer_id)
    return cursor.fetchone()[0] > 0
def load_orders_from_csv(file_path):

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    print("Columns in CSV:", df.columns)
    columns = 'OrderID, CustomerID, EmployeeID, OrderDate, ShipVia, RequiredDate, ShippedDate, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry'
    placeholders = ', '.join('?' * 14)  
    sql_insert_query = f"INSERT INTO Orders ({columns}) VALUES ({placeholders})"
    for index, row in df.iterrows():
        order_id = int(row['OrderID']) if pd.notnull(row['OrderID']) else None
        customer_id = str(row['CustomerID']).strip() if pd.notnull(row['CustomerID']) else None
        if not check_customer_exists(customer_id):
            print(f"Skipping row {index + 1}: CustomerID '{customer_id}' does not exist in the Customers table.")
            continue 
        employee_id = int(row['EmployeeID']) if pd.notnull(row['EmployeeID']) else None
        order_date = pd.to_datetime(row['OrderDate']) if pd.notnull(row['OrderDate']) else None
        ship_via = None
        if 'ShipperID' in df.columns:
            ship_via = int(row['ShipperID']) if pd.notnull(row['ShipperID']) else None
        elif 'ShipVia' in df.columns:
            ship_via = int(row['ShipVia']) if pd.notnull(row['ShipVia']) else None
        required_date = None
        shipped_date = None
        freight = None
        ship_name = None
        ship_address = None
        ship_city = None
        ship_region = None
        ship_postal_code = None
        ship_country = None
        cursor.execute(sql_insert_query, (
            order_id, customer_id, employee_id, order_date, ship_via, 
            required_date, shipped_date, freight, ship_name, ship_address, 
            ship_city, ship_region, ship_postal_code, ship_country
        ))

        print(f"Inserted row {index + 1} into Orders table.")
    conn.commit()

def main():
    csv_path = r"C:\Users\Rabbiya\Desktop\DW LAB\DW LAB\northwind"
    orders_file = "Orders.csv"
    orders_path = os.path.join(csv_path, orders_file)

    load_orders_from_csv(orders_path)
    conn.close()
main()
