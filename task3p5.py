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
def load_customers_from_csv(file_path):
    df = pd.read_csv(file_path)
    columns = 'CustomerID, CompanyName, ContactName, Address, City, PostalCode, Country, Region, Phone, Fax'
    placeholders = ', '.join('?' * 10)
    sql_insert_query = f"INSERT INTO Customers ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        customer_id = str(row['CustomerID']).strip() if 'CustomerID' in df.columns and pd.notnull(row['CustomerID']) else None
        company_name = str(row['CustomerName']).strip() if 'CustomerName' in df.columns and pd.notnull(row['CustomerName']) else None
        contact_name = str(row['ContactName']).strip() if 'ContactName' in df.columns and pd.notnull(row['ContactName']) else None
        address = str(row['Address']).strip() if 'Address' in df.columns and pd.notnull(row['Address']) else None
        city = str(row['City']).strip() if 'City' in df.columns and pd.notnull(row['City']) else None
        postal_code = str(row['PostalCode']).strip() if 'PostalCode' in df.columns and pd.notnull(row['PostalCode']) else None
        country = str(row['Country']).strip() if 'Country' in df.columns and pd.notnull(row['Country']) else None

        region = None
        phone = None
        fax = None
        cursor.execute(sql_insert_query, 
                       (customer_id, company_name, contact_name, address, city, postal_code, country, region, phone, fax))

    conn.commit()
def main():
    csv_path = r"C:\Users\Rabbiya\Desktop\DW LAB\DW LAB\northwind" 
    customers_file = "Customers.csv"  
    customers_path = os.path.join(csv_path, customers_file)
    load_customers_from_csv(customers_path)
    conn.close()
main()