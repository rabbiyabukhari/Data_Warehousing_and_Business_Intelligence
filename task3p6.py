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


def load_suppliers_from_csv(file_path):
    df = pd.read_csv(file_path)

  
    columns = 'SupplierID, CompanyName, ContactName, Address, City, PostalCode, Country, Phone'
    placeholders = ', '.join('?' * 8)
    sql_insert_query = f"INSERT INTO Suppliers ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        supplier_id = int(row['SupplierID']) if 'SupplierID' in df.columns and pd.notnull(row['SupplierID']) else None
        company_name = str(row['SupplierName']).strip() if 'SupplierName' in df.columns and pd.notnull(row['SupplierName']) else None
        contact_name = str(row['ContactName']).strip() if 'ContactName' in df.columns and pd.notnull(row['ContactName']) else None
        address = str(row['Address']).strip() if 'Address' in df.columns and pd.notnull(row['Address']) else None
        city = str(row['City']).strip() if 'City' in df.columns and pd.notnull(row['City']) else None
        postal_code = str(row['PostalCode']).strip() if 'PostalCode' in df.columns and pd.notnull(row['PostalCode']) else None
        country = str(row['Country']).strip() if 'Country' in df.columns and pd.notnull(row['Country']) else None
        phone = str(row['Phone']).strip() if 'Phone' in df.columns and pd.notnull(row['Phone']) else None
        cursor.execute(sql_insert_query, 
                       (supplier_id, company_name, contact_name, address, city, postal_code, country, phone))
    conn.commit()
def main():
    csv_path = r"C:\Users\Rabbiya\Desktop\DW LAB\DW LAB\northwind"  
    suppliers_file = "Suppliers.csv"
    suppliers_path = os.path.join(csv_path, suppliers_file)
    load_suppliers_from_csv(suppliers_path)
    conn.close()
main()