import pyodbc
import pandas as pd
import os
#part2
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-B0IU82M\\SQLEXPRESS;"  
    "Database=Northwind_Rabbiya;"  
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

def load_categories_from_csv(file_path):
    df = pd.read_csv(file_path)
    columns = 'CategoryID, CategoryName, Description, Picture'
    placeholders = ', '.join('?' * 4)
    sql_insert_query = f"INSERT INTO Categories ({columns}) VALUES ({placeholders})"
    for _, row in df.iterrows():
        category_id_str = str(row.iloc[0]).strip()  
        category_name = str(row.iloc[1]).strip()    
        description = ' '.join([str(item) for item in row.iloc[2:] if pd.notnull(item)])
        category_id = int(category_id_str)
        cursor.execute(sql_insert_query, (category_id, category_name, description, None))
    conn.commit()
    
def main():
    csv_path = r"C:\Users\Rabbiya\Desktop\DW LAB\DW LAB\northwind"
    categories_file = "Categories.csv"
    categories_path = os.path.join(csv_path, categories_file)
    load_categories_from_csv(categories_path)
    conn.close()
main()