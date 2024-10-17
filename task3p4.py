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

def load_data_from_csv(table_name, file_path):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip')
        print(f"Data loaded from {file_path} successfully!")
        df = df.dropna()
        columns = ', '.join(df.columns)
        placeholders = ', '.join('?' * len(df.columns))
        sql_insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        for index, row in df.iterrows():
            if table_name == "Shippers":
                cursor.execute("SELECT COUNT(1) FROM Shippers WHERE ShipperID = ?", row['ShipperID'])
                if cursor.fetchone()[0] > 0:
                    print(f"Skipping duplicate ShipperID: {row['ShipperID']}")
                    continue
            cursor.execute(sql_insert_query, tuple(row))
        conn.commit()
        print(f"Data inserted into {table_name} successfully!")
    except Exception as e:
        print(f"Error processing {file_path} for table {table_name}: {e}")


csv_folder_path = r"C:\Users\Rabbiya\Desktop\DW LAB\DW LAB\northwind"
csv_files = {
    "Shippers": "Shippers.csv",
}
for table_name, csv_file in csv_files.items():
    file_path = os.path.join(csv_folder_path, csv_file)
    if os.path.exists(file_path):
        load_data_from_csv(table_name, file_path)
    else:
        print(f"File {file_path} not found!")
conn.close()
print("All data loaded and connection closed.")
